import joblib
import numpy as np
from datetime import datetime

# Load the trained model
model = joblib.load("model/weather_model.pkl")

# Get user input for date
date_input = input("Enter future date (YYYY-MM-DD): ")

# Convert input date to numeric format
date_numeric = datetime.strptime(date_input, "%Y-%m-%d").timetuple().tm_yday  # Convert to day of year

# Convert input into NumPy array and reshape for prediction
input_features = np.array([[date_numeric]])

# Predict weather parameters
predicted_values = model.predict(input_features)[0]

# Display results
print("\n🌤️ **Predicted Weather Conditions**:")
print(f"🌡️ Minimum Temperature: {predicted_values[0]:.2f} °C")
print(f"🌡️ Maximum Temperature: {predicted_values[1]:.2f} °C")
print(f"💨 Wind Speed: {predicted_values[2]:.2f} km/h")
print(f"💧 Relative Humidity: {predicted_values[3]:.2f} %")
print(f"🌧️ Precipitation: {predicted_values[4]:.2f} mm")
