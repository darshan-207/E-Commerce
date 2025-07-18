let currentSlide = 0;
const slides = document.querySelectorAll('.img');
const totalSlides = slides.length;
const slideWidth = slides[0].offsetWidth + 20; // Width of slide + margin
const slideInterval = 2500; // Interval between slides in milliseconds

function nextSlide() {
  const offset = -slideWidth * currentSlide;
  document.querySelector('.rad-slides').style.transform = `translateX(${offset}px)`;
  currentSlide = (currentSlide + 1) % totalSlides;

  setTimeout(nextSlide, slideInterval);
}

// Show the first slide initially
nextSlide();
