#!/usr/bin/env node

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

const {
  GOOGLE_CLIENT_ID,
  GOOGLE_CLIENT_SECRET,
  GOOGLE_REFRESH_TOKEN,
  GBP_ACCOUNT_ID,
  GBP_LOCATION_ID,
} = process.env;

const reviewFile = process.argv[2] || "content-review-2026-05-17-dental-office-server-issues.md";

for (const [name, value] of Object.entries({
  GOOGLE_CLIENT_ID,
  GOOGLE_CLIENT_SECRET,
  GOOGLE_REFRESH_TOKEN,
  GBP_ACCOUNT_ID,
  GBP_LOCATION_ID,
})) {
  if (!value) {
    console.error(`Missing ${name}.`);
    process.exit(1);
  }
}

function extractSection(markdown, heading, nextHeading) {
  const escaped = heading.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const next = nextHeading ? nextHeading.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") : "$";
  const pattern = nextHeading
    ? new RegExp(`## ${escaped}\\s*\\n\\s*([\\s\\S]*?)\\s*## ${next}`)
    : new RegExp(`## ${escaped}\\s*\\n\\s*([\\s\\S]*)$`);
  const match = markdown.match(pattern);
  return match ? match[1].trim() : "";
}

async function request(method, url, { headers = {}, body } = {}) {
  const res = await fetch(url, { method, headers, body });
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
}

async function getAccessToken() {
  const body = new URLSearchParams({
    client_id: GOOGLE_CLIENT_ID,
    client_secret: GOOGLE_CLIENT_SECRET,
    refresh_token: GOOGLE_REFRESH_TOKEN,
    grant_type: "refresh_token",
  });

  const data = await request("POST", "https://oauth2.googleapis.com/token", {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });

  return data.access_token;
}

async function main() {
  const markdown = fs.readFileSync(reviewFile, "utf8");
  const summary = extractSection(
    markdown,
    "Google Business Profile Post Draft",
    "LinkedIn Company Page Post Draft",
  );

  if (!summary) {
    throw new Error(`Could not find Google Business Profile Post Draft in ${reviewFile}`);
  }

  const urlMatch = summary.match(/https:\/\/flossbyte\.com\/\S+/);
  const blogUrl = urlMatch ? urlMatch[0] : "https://flossbyte.com/blog/";

  if (summary.length > 1500) {
    throw new Error(`Google Business post is ${summary.length} characters; max is 1500.`);
  }

  const accessToken = await getAccessToken();
  const endpoint =
    `https://mybusiness.googleapis.com/v4/accounts/${GBP_ACCOUNT_ID}` +
    `/locations/${GBP_LOCATION_ID}/localPosts`;

  const payload = {
    languageCode: "en-US",
    summary,
    callToAction: {
      actionType: "LEARN_MORE",
      url: blogUrl,
    },
  };

  console.log(`Posting to GBP account ${GBP_ACCOUNT_ID}, location ${GBP_LOCATION_ID}...`);

  const result = await request("POST", endpoint, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
