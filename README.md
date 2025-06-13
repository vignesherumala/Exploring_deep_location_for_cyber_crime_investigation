
# 🕵️‍♂️ Exploring Deep Location for Cyber Crime Investigation

A full-stack machine learning web application that predicts potential crimes based on location and time input. It uses a trained Random Forest model and integrates real-time geolocation with Flask, GeoPy, and a responsive frontend.

---

## 🌐 Live Demo

https://exploring-deep-location-for-cyber-crime.onrender.com

---

## 📌 Features

- Accepts user input: address + timestamp
- Converts address to latitude & longitude using **GeoPy**
- Extracts time-based features (hour, day, month, etc.)
- Predicts crime types like Robbery, Murder, Accident, etc.
- Outputs prediction using a clean web interface built with Flask and HTML

---

## 🧰 Tech Stack

### 💻 Frontend:
- HTML, CSS, Bootstrap
- Jinja2 templating engine

### 🧠 Backend:
- Python, Flask
- GeoPy (Nominatim)
- scikit-learn (Random Forest Classifier)
- pandas, NumPy, joblib

### 🧪 Tools:
- Jupyter Notebook
- Git, GitHub
- VS Code, Anaconda

---

## 🗂️ Folder Structure

```
.
├── app.py                 # Main Flask application
├── model/
│   └── rf_model           # Trained ML model saved using joblib
├── templates/
│   ├── index.html         # Input form
│   ├── result.html        # Prediction output
├── static/
│   └── images/            # Static files like team images
├── data.csv               # Dataset used for training
├── CrimePrediction.ipynb  # Model training notebook
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App
```bash
python app.py
```

### 5. Open in Browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📈 Model Overview

- Trained using `RandomForestClassifier`
- Features used: `month`, `day`, `hour`, `latitude`, `longitude`, etc.
- Labels: Robbery, Murder, Gambling, Violence, Accident, Kidnapping
- Model saved in `model/rf_model` using `joblib`

---

## 👤 Author

- **Vignesh Erumala**

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, or distribute.

---

> 💡 _For any suggestions or contributions, feel free to fork this repo or raise an issue!_
