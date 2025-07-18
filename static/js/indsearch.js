// indsearch.js

// Function to redirect to the collection page with a search hash
function redirectToCollectionPage() {
  // Redirects to collection.html with the #search hash
  window.location.href = '/templates/collection.html#search';
}

// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Get the search input element
  var searchInput = document.getElementById('search');
  
  // Add an event listener to the search input for the 'click' event
  searchInput.addEventListener('click', redirectToCollectionPage);
  
  // Check if the URL has a hash of #search
  if (window.location.hash === '#search') {
      // Focus on the search input if the hash is #search
      searchInput.focus();
  }
});
