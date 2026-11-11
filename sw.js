const C="a1-v11",A="a1-audio-v1",F=["./","index.html","content.js","manifest.json","icon.svg","icon-192.png","icon-512.png","audio/index.json"];
self.addEventListener("install",e=>{self.skipWaiting();e.waitUntil(caches.open(C).then(c=>c.addAll(F)))});
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C&&x!==A).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{
  const u=new URL(e.request.url);
  // Audio packs never change for a given name: serve from cache, fetch once.
  if(u.pathname.includes("/audio/")&&u.pathname.endsWith(".mp3")){
    e.respondWith(caches.open(A).then(c=>c.match(e.request.url).then(h=>h||fetch(e.request.url).then(r=>{if(r.ok)c.put(e.request.url,r.clone());return r}))));return}
  e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));
});
