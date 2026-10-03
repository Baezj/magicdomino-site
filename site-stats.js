// ==================================================================================
// Anonymous page counts for magicdomino.com (see the privacy policy, priv.s1.li8).
//
// One note per page view — which page, the browser's language — and one per store
// button tap. NO cookie, NO identifier, nothing written to the browser. It goes to the
// same Worker the app uses (stats.magicdomino.com), whose schema.json allows only
// these two events with these fields. Do Not Track / Global Privacy Control → nothing.
// ==================================================================================
(function () {
  "use strict";
  if (navigator.globalPrivacyControl === true || navigator.doNotTrack === "1" || window.doNotTrack === "1") return;
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
    var body = JSON.stringify({ v: 1, platform: "web", channel: "release", events: events });
    try {
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPOINT, body)) return;
      fetch(ENDPOINT, { method: "POST", body: body, keepalive: true, mode: "cors", credentials: "omit" });
    } catch (e) { /* never break the page over a count */ }
  }

  // After i18n.js has set the page language.
  window.addEventListener("load", function () {
    send([{ n: "web_view", d: day(), p: { page: page(), lang: lang() } }]);
  });
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var target = /apps\.apple\.com/.test(a.href) ? "appstore" : /play\.google\.com/.test(a.href) ? "googleplay" : null;
    if (target) send([{ n: "web_click", d: day(), p: { target: target, page: page() } }]);
  }, true);
})();
