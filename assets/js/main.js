// Smooth scrolling sliders
document.querySelectorAll('.slider').forEach(slider => {
  slider.style.scrollBehavior = 'smooth';
  slider.style.webkitOverflowScrolling = 'touch';
});