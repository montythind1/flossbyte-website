#!/usr/bin/env node

const http = require("node:http");
const fs = require("node:fs");

function loadDotEnv(path = ".env") {
  if (!fs.existsSync(path)) return;

  const lines = fs.readFileSync(path, "utf8").split(/\r?\n/);
  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const separator = trimmed.indexOf("=");
    if (separator === -1) continue;

    const key = trimmed.slice(0, separator).trim();
    const value = trimmed.slice(separator + 1).trim().replace(/^["']|["']$/g, "");
    if (key && process.env[key] === undefined) {
      process.env[key] = value;
    }
  }
}

loadDotEnv();

const SCOPES = ["https://www.googleapis.com/auth/business.manage"];
const clientId = process.env.GOOGLE_CLIENT_ID;
const clientSecret = process.env.GOOGLE_CLIENT_SECRET;

if (!clientId || !clientSecret) {
  console.error("Missing GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET.");
  console.error("Set them in your shell first, or load them from a local .env file.");
  process.exit(1);
}

function request(method, url, { headers = {}, body } = {}) {
  return fetch(url, { method, headers, body }).then(async (res) => {
    const text = await res.text();
    let data;
    try {
      data = text ? JSON.parse(text) : {};
    } catch {
      data = text;
    }

    if (!res.ok) {
      const detail = typeof data === "string" ? data : JSON.stringify(data, null, 2);
      throw new Error(`${method} ${url} failed (${res.status}): ${detail}`);
    }

    return data;
  });
}

function waitForOAuthCode(server) {
  return new Promise((resolve, reject) => {
    server.on("request", (req, res) => {
      try {
        const url = new URL(req.url, `http://${req.headers.host}`);
        if (url.pathname !== "/oauth2callback") {
          res.writeHead(404);
          res.end("Not found");
          return;
        }

        const error = url.searchParams.get("error");
        if (error) {
          res.writeHead(400, { "Content-Type": "text/plain" });
          res.end(`Google OAuth error: ${error}`);
          reject(new Error(error));
          return;
        }

        const code = url.searchParams.get("code");
        if (!code) {
          res.writeHead(400, { "Content-Type": "text/plain" });
          res.end("Missing OAuth code.");
          reject(new Error("Missing OAuth code"));
          return;
        }

        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end("Google authorization received. You can return to Codex.");
        resolve(code);
      } catch (err) {
        reject(err);
      }
    });
  });
}

async function main() {
  const server = http.createServer();
  server.listen(0, "127.0.0.1");

  await new Promise((resolve) => server.once("listening", resolve));
  const { port } = server.address();
  const redirectUri = `http://127.0.0.1:${port}/oauth2callback`;

  const authUrl = new URL("https://accounts.google.com/o/oauth2/v2/auth");
  authUrl.searchParams.set("client_id", clientId);
  authUrl.searchParams.set("redirect_uri", redirectUri);
  authUrl.searchParams.set("response_type", "code");
  authUrl.searchParams.set("scope", SCOPES.join(" "));
  authUrl.searchParams.set("access_type", "offline");
  authUrl.searchParams.set("prompt", "consent");

  console.log("\nOpen this URL in a browser signed into the Google account that manages FlossByte GBP:\n");
  console.log(authUrl.toString());
  console.log("\nWaiting for Google OAuth callback...\n");

  try {
    const code = await waitForOAuthCode(server);

    const tokenBody = new URLSearchParams({
      code,
      client_id: clientId,
      client_secret: clientSecret,
      redirect_uri: redirectUri,
      grant_type: "authorization_code",
    });

    const tokens = await request("POST", "https://oauth2.googleapis.com/token", {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: tokenBody,
    });

    if (!tokens.refresh_token) {
      console.warn("No refresh_token returned. Re-run with prompt=consent or revoke prior app consent.");
    }

    const authHeaders = { Authorization: `Bearer ${tokens.access_token}` };
    const accountsResponse = await request(
      "GET",
      "https://mybusinessaccountmanagement.googleapis.com/v1/accounts",
      { headers: authHeaders },
    );

    const accounts = accountsResponse.accounts || [];
    const discovery = {
      generatedAt: new Date().toISOString(),
      refreshToken: tokens.refresh_token || null,
      accounts: [],
    };

    for (const account of accounts) {
      const locationsUrl =
        `https://mybusinessbusinessinformation.googleapis.com/v1/${account.name}/locations?` +
        new URLSearchParams({
          readMask: "name,title,storefrontAddress,metadata",
        });

      let locations = [];
      try {
        const locationsResponse = await request("GET", locationsUrl, { headers: authHeaders });
        locations = locationsResponse.locations || [];
      } catch (err) {
        locations = [{ error: err.message }];
      }

      discovery.accounts.push({
        name: account.name,
        accountId: account.name.replace("accounts/", ""),
        accountName: account.accountName,
        type: account.type,
        locations: locations.map((location) => {
          if (location.error) return location;
          return {
            name: location.name,
            locationId: location.name.replace("locations/", ""),
            title: location.title,
            address: location.storefrontAddress,
            mapsUri: location.metadata?.mapsUri,
          };
        }),
      });
    }

    fs.writeFileSync("gbp-discovery.json", JSON.stringify(discovery, null, 2));

    console.log("GBP discovery saved to gbp-discovery.json (gitignored).");
    console.log("\nAdd these values to your local .env after choosing the correct profile:\n");
    if (tokens.refresh_token) {
      console.log(`GOOGLE_REFRESH_TOKEN=${tokens.refresh_token}`);
    }

    for (const account of discovery.accounts) {
      console.log(`# Account: ${account.accountName || account.name}`);
      console.log(`GBP_ACCOUNT_ID=${account.accountId}`);
      for (const location of account.locations) {
        if (location.error) {
          console.log(`# Location fetch error: ${location.error}`);
          continue;
        }
        console.log(`# Location: ${location.title || location.name}`);
        console.log(`GBP_LOCATION_ID=${location.locationId}`);
      }
      console.log("");
    }
  } finally {
    server.close();
  }
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
