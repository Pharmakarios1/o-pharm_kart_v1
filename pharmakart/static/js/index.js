// JavaScript code for managing the shopping cart
  let  cartItems = [];
  let cartTotal = 0;

  function addToCart(productName, productPrice) {
      cartItems.push({ name: productName, price: productPrice });
      cartTotal += productPrice;
      updateCartUI();
  }

  function removeFromCart(index) {
      let removedItem = cartItems.splice(index, 1)[0];
      cartTotal -= removedItem.price;
      updateCartUI();
  }

  function updateCartUI() {
      let cartItemsContainer = document.getElementById('cart-items');
      let  cartTotalElement = document.getElementById('cart-total');

      cartItemsContainer.innerHTML = ''; // Clear the cart items list

      cartItems.forEach((item, index) => {
          let  cartItemDiv = document.createElement('div');
          cartItemDiv.className = 'cart-item';
          cartItemDiv.innerHTML = `
              <span>${item.name} - $${item.price.toFixed(2)}</span>
              <button onclick="removeFromCart(${index})">Remove</button>
          `;
          cartItemsContainer.appendChild(cartItemDiv);
      });

      cartTotalElement.textContent = cartTotal.toFixed(2);
  }

//   modal
var myModal = new bootstrap.Modal(document.getElementById('myModal'));
myModal.show();



 // Get references to the select element and submit button
 const medicationSelect = document.getElementById("medicationSelect");
 const submitButton = document.getElementById("submitButton");

 submitButton.addEventListener("click", () => {
   if (medicationSelect.value === "2") {
     document.getElementById("meds").scrollIntoView({ behavior: "smooth" });
   }
 });





