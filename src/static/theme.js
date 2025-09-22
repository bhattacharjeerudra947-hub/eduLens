// Apply saved theme on page load
    window.onload = function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.getElementById('themeStylesheet').setAttribute('href', savedTheme);
      }
      };

    // Toggle theme and save preference
    function toggleTheme() {
    const themeLink = document.getElementById('themeStylesheet');
    const currentTheme = themeLink.getAttribute('href');

    const lightTheme = "/static/main.css";
    const darkTheme = "/static/dark.css";

    const newTheme = currentTheme.includes("main.css") ? darkTheme : lightTheme;
    themeLink.setAttribute('href', newTheme);
    localStorage.setItem('theme', newTheme);
    }