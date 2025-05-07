const CACHE_NAME = "sweetleaf-v1";
const urlsToCache = [
  "/sweetleaf-co/",
  "/sweetleaf-co/index.html",
  "/sweetleaf-co/static/bootstrap.min.css",
  "/sweetleaf-co/static/sweetleaf.css",
  "/sweetleaf-co/static/assets/hero.jpg",
  "/sweetleaf-co/static/assets/favicon.jpg",
  "/sweetleaf-co/static/assets/mint.jpg",
  "/sweetleaf-co/static/assets/chamomile.jpg",
  "/sweetleaf-co/static/assets/earlgrey.jpg",
  "/sweetleaf-co/static/assets/hibiscous.jpg"
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
