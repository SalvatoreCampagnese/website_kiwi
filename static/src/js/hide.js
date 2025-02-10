odoo.define("kiwi_theme.hideHeaderFooter", [], function (require) {
  "use strict";
  // If location is /web/login, hide header and footer
  if (window.location.pathname === "/web/login") {
    document.querySelector("header").style.display = "none";
    document.querySelector("footer").style.display = "none";
  }
});
