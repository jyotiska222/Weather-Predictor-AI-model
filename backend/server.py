from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime
from flask_cors import CORS  # To allow React to access API

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load trained model
model = joblib.load("model/model/weather_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        date_input = data.get("date")

        # Convert input date to numeric format (day of year)
        date_numeric = datetime.strptime(date_input, "%Y-%m-%d").timetuple().tm_yday  
        input_features = np.array([[date_numeric]])

        # Predict weather parameters
        predicted_values = model.predict(input_features)[0]

        # Return predictions as JSON
        response = {
            "date": date_input,
            "min_temp": round(predicted_values[0], 2),
            "max_temp": round(predicted_values[1], 2),
            "wind_speed": round(predicted_values[2], 2),
            "humidity": round(predicted_values[3], 2),
            "precipitation": round(predicted_values[4], 2),
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
