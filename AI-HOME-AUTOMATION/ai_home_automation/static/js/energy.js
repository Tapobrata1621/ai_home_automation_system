document.addEventListener("DOMContentLoaded", function () {

    const ctx = document.getElementById("energyChart");

    if (!ctx) return;

    // Example data from Flask (replace with your real values)
    const data = [3.4, 2.8, 3.6, 2.9, 3.2, 3.8, 4.0];
    const labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Energy (kWh)",
                data: data,
                borderColor: "#6a8dff",
                backgroundColor: "rgba(106, 141, 255, 0.25)",
                borderWidth: 3,
                tension: 0.4,
                pointRadius: 5,
                pointBackgroundColor: "#6a8dff"
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { color: "#5a5a5a" },
                    grid: { color: "#e8eaf3" }
                },
                x: {
                    ticks: { color: "#5a5a5a" },
                    grid: { display: false }
                }
            }
        }
    });

});
