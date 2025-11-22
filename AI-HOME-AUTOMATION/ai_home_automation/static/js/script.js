// Theme toggle: persist to localStorage
const checkbox = document.getElementById('themeToggle');
const root = document.documentElement;

if (localStorage.getItem('dark') === 'true') {
  document.documentElement.classList.add('dark');
  if (checkbox) checkbox.checked = true;
}

if (checkbox) {
  checkbox.addEventListener('change', () => {
    if (checkbox.checked) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('dark', 'true');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('dark', 'false');
    }
  });
}

// Energy chart (Chart.js)
const ctx = document.getElementById('energyChart');
if (ctx) {
  const labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  const data = {
    labels,
    datasets: [{
      label: 'kWh',
      data: [3.2, 2.8, 3.6, 3.0, 2.5, 2.9, 3.4],
      borderRadius: 6,
      barThickness: 18,
      backgroundColor: (ctx && ctx.closest('html').classList.contains('dark')) ? '#60a5fa' : '#2b7cff',
      maxBarThickness: 24
    }]
  };
  new Chart(ctx, {
    type: 'bar',
    data,
    options: {
      plugins: { legend: { display: false } },
      scales: {
        x: { grid:{display:false}, ticks:{color: getComputedStyle(document.documentElement).getPropertyValue('--muted')} },
        y: { grid:{color: 'rgba(0,0,0,0.04)'}, ticks:{color: getComputedStyle(document.documentElement).getPropertyValue('--muted')} }
      }
    }
  });
}
