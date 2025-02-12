import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from datetime import datetime

# Load dataset
file_path = "../data/kolkata_weather.csv"  # Change this to your actual dataset file path
data = pd.read_csv(file_path)

# Convert Date to Numeric Format
data["Date time"] = pd.to_datetime(data["Date time"])  # Convert to datetime
data["DayOfYear"] = data["Date time"].dt.dayofyear  # Convert to day of year

# Select Features (Date) and Targets (Weather parameters)
features = ["DayOfYear"]  # Only date as feature
target = ["Minimum Temperature", "Maximum Temperature", "Wind Speed", "Relative Humidity", "Precipitation"]

# Drop missing values
data = data[features + target].dropna()

# Split dataset
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n✅ Model training completed!")
print(f"📊 MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")

# Save the trained model
joblib.dump(model, "model/weather_model.pkl")
print("✅ Model saved as 'model/weather_model.pkl'")
