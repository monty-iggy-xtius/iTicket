const observer = new IntersectionObserver(entries => {
  // Loop over the entries
  entries.forEach(entry => {
    // If the element is visible
    if (entry.isIntersecting) {
      // Add the animation class
      entry.target.classList.add('custom-down-animation-div');
    }
  });
});

// observer.observe(document.querySelector('.pref-items'));

// instead of one element, get all because there are multiple of them
document.querySelectorAll('.pref-items').forEach((target) => {
  observer.observe(target)
})
