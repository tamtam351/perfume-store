document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');
    
    // Toggle menu when hamburger is clicked
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        navMenu.classList.toggle('active');
    });
    
    // Close menu when clicking a nav link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const carousel = document.querySelector(".carousel");
  
    gsap.to(carousel, {
      xPercent: -100,
      duration: 10,
      repeat: -1,
      ease: "linear",
      modifiers: {
        xPercent: gsap.utils.wrap(-100, carousel.children.length * -100),
      },
    });
  });
  