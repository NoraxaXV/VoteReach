/*
A Cookie is a way of storing data when a user vists a page.
When they visit and sign up, we can remember their username for when they return.
*/ 

var Cookie = {
  // Sets a cookie's values, parameters are the name of the cookie, the values being set to the cookie, and the number of days we want to remeber this cookie
  set: function (cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }

  // Gets a cookie by its name. Returns either a value or an empty string
  get: function (cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
}


