// Adds momentum scroll on iOS & hides scrollbar
document.querySelectorAll('.slider').forEach(slider => {
  slider.style.scrollBehavior = 'smooth';
  slider.style.webkitOverflowScrolling = 'touch';
});