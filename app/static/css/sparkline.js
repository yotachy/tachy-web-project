function drawSparkline(el) {
  const raw = (el.dataset.values || "").trim();
  if (!raw) {
    console.warn("[sparkline] missing data-values", el);
    return;
  }

  const values = raw
    .split(",")
    .map(v => Number(v.trim()))
    .filter(v => Number.isFinite(v));

  if (values.length < 2) {
    console.warn("[sparkline] not enough values", raw, el);
    return;
  }

  const width = 120;
  const height = 32;
  const pad = 2;

  const min = Math.min(...values);
  const max = Math.max(...values);
  const span = (max - min) || 1;

  const xStep = (width - pad * 2) / (values.length - 1);

  const points = values.map((v, i) => {
    const x = pad + i * xStep;
    const y = pad + (height - pad * 2) * (1 - (v - min) / span);
    return `${x.toFixed(2)},${y.toFixed(2)}`;
  });

  const up = values[values.length - 1] >= values[0];

  el.innerHTML = `
    <svg viewBox="0 0 ${width} ${height}" preserveAspectRatio="none" aria-hidden="true">
      <polyline class="sparkline__line ${up ? "is-up" : "is-down"}"
        points="${points.join(" ")}" />
    </svg>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  const nodes = document.querySelectorAll("[data-sparkline]");
  console.log("[sparkline] found", nodes.length);
  nodes.forEach(drawSparkline);
});
