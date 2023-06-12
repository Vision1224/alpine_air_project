document.addEventListener("DOMContentLoaded", function () {
  fetch("/orders_data")
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.querySelector("#ordersTable tbody");
      data.forEach((order) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${String(order.model_number)}</td>
          <td>${String(order.unit_price)}</td>
          <td>${String(order.quantity)}</td>
        `;
        tableBody.appendChild(row);
      });
    });
});
