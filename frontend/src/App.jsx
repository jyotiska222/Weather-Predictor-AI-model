import { useState } from "react";
import "./App.css";

function App() {
  const [date, setDate] = useState("");
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchWeather = async () => {
    if (!date) {
      setError("Please enter a valid date.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ date }),
      });

      if (!response.ok) throw new Error("Failed to fetch weather data");

      const data = await response.json();
      setWeatherData(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🌤️ Weather Predictor</h1>
      <p>Enter a future date to get weather predictions.</p>

      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />
      <button onClick={fetchWeather} disabled={loading}>
        {loading ? "Predicting..." : "Get Forecast"}
      </button>

      {error && <p className="error">{error}</p>}

      {weatherData && (
        <div className="weather-result">
          <h2>Predicted Weather on {date}</h2>
          <p>🌡️ Min Temp: {weatherData.min_temp}°C</p>
          <p>🌡️ Max Temp: {weatherData.max_temp}°C</p>
          <p>💨 Wind Speed: {weatherData.wind_speed} km/h</p>
          <p>💧 Humidity: {weatherData.humidity}%</p>
          <p>🌧️ Precipitation: {weatherData.precipitation} mm</p>
        </div>
      )}
    </div>
  );
}

export default App;
