
const CACHE_NAME = 'cache-v1';

// List static assets to cache
const staticAssets = [
  '/static/css/index-styles.css',
  '/static/css/index-stylesheet.css',
  '/static/js/index-script.js',
  '/static/images/shopping-bag.jpg',
  '/static/images/img/favicon.ico',
  '/static/images/img/team/spongebob.jpg',
  '/static/images/img/team/sandy.jpg',
  '/static/images/img/team/patrick.jpg',
  '/static/images/img/team/crabs.jpg',
  '/static/images/products/1.jpg',
  '/static/images/products/2.jpg',
  '/static/images/products/3.png',
  '/static/images/products/4.png',
  '/static/images/products/5.png',
  '/static/images/products/6.png',
  '/static/images/products/7.png',
  '/static/images/products/8.png',
  '/static/images/products/9.png',
  '/static/images/products/10.png',
  '/static/images/products/11.png',
  '/static/images/products/12.png',
  '/static/images/products/13.png',
  '/static/images/products/14.png',
  '/static/images/products/15.png',
  '/static/images/products/placeholder.png',
  '/static/images/192chocopinklogo1.png',
  '/static/images/512logop1sprinkles.png'

//   'https://cdn.startbootstrap.com/sb-forms-latest.js'
];

// Cache static assets during the service worker installation
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      await cache.addAll(staticAssets);
      const response = await fetch('/');
      cache.put('/', response);
    })
  );
});


// Fetch and cache dynamic assets (e.g., product images and descriptions)
self.addEventListener('fetch', (event) => {
    event.respondWith(
      caches.match(event.request).then((response) => {
        if (response) {
          return response;
        }

        // Serve the cached index.html file for the root path
          if (event.request.url.endsWith('/')) {
            return caches.match('/index.html');
          }

        return fetch(event.request).catch(() => {
          //fallback for the external JS library
          if (event.request.url === 'https://cdn.startbootstrap.com/sb-forms-latest.js') {
            return new Response('', { headers: { 'Content-Type': 'text/javascript' } });
          }
        }).then((networkResponse) => {
          if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
            return networkResponse;
          }

          const clonedResponse = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, clonedResponse);
          });

          return networkResponse;
        });
      })
    );
  });


// Update and clean up old caches during service worker activation
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
