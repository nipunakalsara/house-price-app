# 🏠 House Price Prediction App

A machine learning web application built with **Streamlit** that predicts California house prices based on key features.

---

## 📸 Demo

> Enter house details → Click Predict → Get instant price estimate!

---

## 🚀 Features

- Predict house prices instantly using a trained ML model
- Simple and clean user interface
- Built with Python and Streamlit
- Uses the California Housing Dataset

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming Language |
| Streamlit | Web App Framework |
| Scikit-learn | Machine Learning Model |
| NumPy | Numerical Computing |
| Joblib | Model Serialization |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/nipunakalsara/house-price-app.git
cd house-price-app
```

### 2. Install dependencies
```bash
pip install streamlit numpy joblib scikit-learn
```

### 3. Download the model file
The model file (`house_price_model.pkl`) is not included in the repo due to its size.

👉 Download it from: `[Add your Google Drive link here]`

Place it in the same folder as `app.py`.

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at: `http://localhost:8501`

---

## 📋 Input Features

| Feature | Description |
|--------|-------------|
| Median Income | Median income of households in the area |
| House Age | Age of the house in years |
| Average Rooms | Average number of rooms per household |
| Average Bedrooms | Average number of bedrooms per household |
| Population | Population of the block |
| Average Occupancy | Average number of people per household |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

---

## 📁 Project Structure

```
house-price-app/
├── app.py                  # Main Streamlit app
├── house_price_model.pkl   # Trained ML model (download separately)
├── .gitignore
└── README.md
```

---

## 👨‍💻 Author

**Nipuna Kalsara**
- GitHub: [@nipunakalsara](https://github.com/nipunakalsara)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
