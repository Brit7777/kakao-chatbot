var http = require("http");
setInterval(function() {
    http.get("http://mighty-spire-71391.herokuapp.com");
}, 300000); // every 5 minutes (300000)