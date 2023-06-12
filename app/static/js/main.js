document
  .getElementById("purchaseOrderForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Get form data
    const form = document.getElementById("purchaseOrderForm");
    const formData = new FormData(form);

    // Send form data to the backend
    fetch("/", {
      // Update the URL to match the root URL of the backend
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        // Display response from the backend
        const responseDiv = document.getElementById("response");
        responseDiv.innerHTML = data;
        responseDiv.style.display = "block";
      })

      .catch((error) => console.error(error));
  });
