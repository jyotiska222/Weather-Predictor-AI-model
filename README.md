# 🌦️ Weather Prediction Web App

This project is a **machine learning-powered weather prediction web app** that forecasts weather conditions based on historical data for **Kolkata**. The backend uses **Linear Regression** to predict parameters like **temperature, wind speed, humidity, and precipitation**.

---

## 🚀 Features
✅ Predict **Minimum & Maximum Temperature**  
✅ Forecast **Wind Speed, Humidity, and Precipitation**  
✅ Uses **Cyclical Encoding (sin/cos)** for accurate date-based predictions  
✅ **User-friendly Web UI** for easy input and visualization  
✅ **REST API** for predictions  

---

## 🛠️ Tech Stack

### **Frontend:**
- **React.js** (for building the UI)
- **Tailwind CSS** (for styling)
  
### **Backend:**
- **Node.js with Express.js** (API for fetching predictions)
- **Python (Flask/FastAPI)** (for ML model execution)
- **Scikit-Learn, NumPy, Pandas** (for training & predictions)
- **Joblib** (for model persistence)

---

## 📂 Project Structure
```
weatherweb/
│── frontend/               # React.js UI
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page-level components
│   │   ├── App.js          # Main entry file
│   │   ├── index.js        # Renders the app
│   ├── public/             # Static assets
│── backend/                # Backend API
│   ├── model/              # Machine Learning model
│   │   ├── train_model.py  # ML model training
│   │   ├── predict.py      # Prediction script
│   │   ├── weather_model.pkl # Saved ML model
│   ├── routes/             # API endpoints
│   ├── server.js           # Express.js backend
│── data/                   # Weather dataset
│── README.md               # Project Documentation
```

---

## 🔧 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/weatherweb.git
cd weatherweb
```

### **2️⃣ Install Backend Dependencies**
```bash
cd backend
pip install -r requirements.txt  # Install Python dependencies
```

### **3️⃣ Train the Machine Learning Model**
```bash
python model/train_model.py
```
This will train the model using **Linear Regression** and save it as `weather_model.pkl`.

### **4️⃣ Start Backend API**
```bash
python server.py
```
The backend will be running at `http://localhost:5000/`.

### **5️⃣ Install Frontend Dependencies**
```bash
cd ../frontend
npm install
```

### **6️⃣ Start Frontend**
```bash
npm start
```
The React app will be running at `http://localhost:3000/`.

---

## 📌 Usage Guide

1️⃣ Open the web app  
2️⃣ Enter a **future date (YYYY-MM-DD)**  
3️⃣ Click **"Predict"**  
4️⃣ View forecasted **temperature, wind speed, humidity, and precipitation**  

---

## 🛠️ Troubleshooting

### **1️⃣ Model Prediction Error (Feature Mismatch)**
**Error:** `X has 3 features, but LinearRegression is expecting 1 feature as input`  
**Solution:** Make sure that `train_model.py` and `predict.py` use the same **features** (`sin_day`, `cos_day`, `Month`).  

### **2️⃣ Backend API Not Responding**
**Solution:** Ensure the backend is running (`python server.py`). Check logs for errors.

### **3️⃣ Frontend Not Connecting to Backend**
**Solution:** Update API endpoint in `frontend/src/config.js` to match the backend URL (`http://localhost:5000/`).

---

## 🤝 Contributing
Want to improve the project? Feel free to **fork**, **open issues**, and submit **pull requests**! 💡

---

## 💬 Contact
📧 **Your Name** - [j.biswas0022@gmail.com](mailto:j.biswas0022@gmail.com)  

