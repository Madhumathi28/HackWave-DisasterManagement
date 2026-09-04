const API_BASE_URL = "http://127.0.0.1:8000";

export async function simulateFlood(waterLevel) {
  const url =
    `${API_BASE_URL}/api/flood/simulate` +
    `?water_level=${encodeURIComponent(waterLevel)}`;

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(
      `Flood API failed with status ${response.status}`
    );
  }

  return response.json();
}