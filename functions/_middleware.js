export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www.flossbyte.com") {
    url.hostname = "flossbyte.com";
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
