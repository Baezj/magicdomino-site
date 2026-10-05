// ==================================================================================
// Anonymous page counts for magicdomino.com (see the privacy policy, priv.s1.li8).
//
// One note per page view — which page, the browser's language — and one per store
// button tap or Watch Live link tap (the board itself is counted by the relay's stats.js). NO cookie, NO identifier, nothing written to the browser. It goes to the
// same Worker the app uses (stats.magicdomino.com), whose schema.json allows only
// these two events with these fields. Do Not Track / Global Privacy Control → nothing.
//
// ⚠️ ONLY PEOPLE ARE COUNTED, AS FAR AS A PAGE CAN TELL (2026-10-04, Juan: "how do i
//    know thats real people and not a crawler or ai or myself?"):
//    - Crawlers that only fetch HTML never run this file, so they were never counted.
//    - Automated browsers announce themselves (navigator.webdriver) → nothing sent.
//    - A view counts only after the page has been ON SCREEN for 2 seconds: a renderer
//      that loads and leaves, a prerender, a tab opened in the background and closed
//      unseen — none of them count. The Worker also drops anything whose browser
//      says it is a bot or a headless browser.
//    - Juan's own browsers: open magicdomino.com/?me=1 once on each. That browser's
//      notes go to the portal's "My devices" instead of the real numbers (?me=0 undoes
//      it). Nobody else ever has this flag.
// ==================================================================================
(function () {
  "use strict";
  if (navigator.globalPrivacyControl === true || navigator.doNotTrack === "1" || window.doNotTrack === "1") return;
  if (navigator.webdriver === true) return;

  // The owner's switch (see the header). Stored only on a browser that asked for it.
  var OWNER_KEY = "md.statsOwnerTag";
  var ownerTag = null;
  try {
    var me = new URLSearchParams(location.search).get("me");
    if (me === "1" && !localStorage.getItem(OWNER_KEY)) {
      localStorage.setItem(OWNER_KEY, "web" + Math.random().toString(36).slice(2, 10).replace(/[^a-z0-9]/g, "0"));
    } else if (me === "0") {
      localStorage.removeItem(OWNER_KEY);
    }
    ownerTag = localStorage.getItem(OWNER_KEY);
    if (ownerTag && !/^[a-z0-9]{6,24}$/.test(ownerTag)) ownerTag = null;
  } catch (e) { /* storage blocked: counted like anybody else */ }
  var ENDPOINT = "https://stats.magicdomino.com/v1/e";
  var LANGS = ["en", "es", "fr", "pt", "ar", "zh", "nl", "de", "hi", "it", "ja", "ko", "ru", "bn", "id", "ur", "tr"];

  function day() {
    var d = new Date();
    var p = function (n) { return (n < 10 ? "0" : "") + n; };
    return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate());
  }
  function page() {
    var path = location.pathname.replace(/\/+$/, "").replace(/\.html$/, "");
    var name = path === "" || path === "/index" ? "home" : path.split("/").pop().toLowerCase();
    // Known pages only: GitHub Pages serves 404.html for ANY address, and a typed
    // address must never become a stored value.
    return ["home", "privacy", "support", "terms"].indexOf(name) >= 0 ? name : "other";
  }
  function lang() {
    var l = (document.documentElement.lang || navigator.language || "en").slice(0, 2).toLowerCase();
    return LANGS.indexOf(l) >= 0 ? l : "other";
  }
  function send(events) {
    var batch = { v: 1, platform: "web", channel: "release", events: events };
    if (ownerTag) batch.dev = ownerTag;
    var body = JSON.stringify(batch);
    try {
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPOINT, body)) return;
      fetch(ENDPOINT, { method: "POST", body: body, keepalive: true, mode: "cors", credentials: "omit" });
    } catch (e) { /* never break the page over a count */ }
  }

  // After i18n.js has set the page language, and only once the page has been on
  // screen for 2 seconds in a row (hidden → the clock restarts when it is shown).
  var counted = false, timer = null;
  function arm() {
    if (counted || timer || document.visibilityState !== "visible") return;
    timer = setTimeout(function () {
      timer = null;
      if (counted || document.visibilityState !== "visible") return;
      counted = true;
      send([{ n: "web_view", d: day(), p: { page: page(), lang: lang() } }]);
    }, 2000);
  }
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState !== "visible" && timer) { clearTimeout(timer); timer = null; }
    arm();
  });
  if (document.readyState === "complete") arm();
  else window.addEventListener("load", arm);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var target = /apps\.apple\.com/.test(a.href) ? "appstore" : /play\.google\.com/.test(a.href) ? "googleplay"
      : /^\/tv(\/|$)/.test(a.pathname) && a.host === location.host ? "watch" : null;
    if (target) send([{ n: "web_click", d: day(), p: { target: target, page: page() } }]);
  }, true);
})();
