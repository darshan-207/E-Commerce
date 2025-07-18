// index.js

// Function to show side navigation
var sidenav = document.querySelector(".side-navbar");

function showsidenav() {
  sidenav.style.left = "0";
}

function hidesidenav() {
  sidenav.style.left = "-60%";
}

// Function to add an item to cart
function addToCart(itemName) {
  // Retrieve existing cart items from localStorage or initialize as empty array
  let cartItems = JSON.parse(localStorage.getItem('cart')) || [];

  // Check if the item is already in the cart
  if (cartItems.includes(itemName)) {
    alert('Item is already in the cart!');
    return;
  }

  // Add the item to cart
  cartItems.push(itemName);

  // Save updated cart items back to localStorage
  localStorage.setItem('cart', JSON.stringify(cartItems));

  // Update UI or show confirmation
  updateCartUI();
}

// Function to update cart UI
function updateCartUI() {
  // Get the cart count element (assuming you have a cart count display in your HTML)
  let cartCountElement = document.querySelector('#cart-count');

  // Retrieve the updated cart items count
  let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
  let itemCount = cartItems.length;

  // Update the cart count display
  if (cartCountElement) {
    cartCountElement.textContent = itemCount;
  }

  // Optional: Display a confirmation or update UI to reflect added item
  alert('Item added to cart! Total items: ' + itemCount);
}

// Example usage for buttons (if you have buttons with data-item-name attributes)
document.querySelectorAll('.add-to-cart-button').forEach(button => {
  button.addEventListener('click', function() {
    addToCart(this.dataset.itemName);
  });
});
