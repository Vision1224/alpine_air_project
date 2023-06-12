document
  .getElementById("purchaseOrderForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const form = document.getElementById("purchaseOrderForm");
    const formData = new FormData(form);

    fetch("/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        const responseDiv = document.getElementById("response");
        responseDiv.innerHTML = data;
        responseDiv.style.display = "block";
      })

      .catch((error) => console.error(error));
  });
