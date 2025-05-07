const CACHE_NAME = "sweetleaf-v1";
const urlsToCache = [
  "/",
  "/static/bootstrap.min.css",
  "/static/sweetleaf.css",
  "/static/assets/hero.jpg",
  "/static/assets/favicon.jpg",
  "/static/assets/mint.jpg",
  "/static/assets/chamomile.jpg",
  "/static/assets/earl_grey.jpg",
  "/static/assets/hibiscus.jpg"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
