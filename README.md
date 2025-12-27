# 🏡 House Price Prediction System

A **Machine Learning-based house price prediction app** built using Python and Streamlit.  
This project predicts house prices based on user-selected property details such as location, total area, BHK, and number of bathrooms using a trained ML model.

---

## 🚀 Features

- 🔍 **Real-time Price Prediction**  
- 📍 Predict prices based on **Location, Area, BHK, and Bathrooms**  
- ⚡ **Fast, interactive UI** using Streamlit  
- 💾 **Pre-trained ML model** stored with Pickle  
- 🎨 Stylish and responsive design with colorful gradients  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- NumPy / Pandas  
- Scikit-Learn  
- Pickle (for model storage)  

---
📁 Project Structure ├── app.py ├── movies.pkl ├── requirements.txt ├── README.md └── images/ (optional screenshots)

🔧 Installation & Setup 1️⃣ Clone the repository git clone https://github.com/PanchalArti/house_price_predection.git cd house_price_prediction

2️⃣ Install Dependencies pip install -r requirements.txt

3️⃣ Run Streamlit App streamlit run app.py

🖼️ Screenshots

![App Screenshot](https://github.com/PanchalArti/house_price_predection/blob/main/snapshot1.png)

![App Screenshot](https://github.com/PanchalArti/house_price_predection/blob/main/snaoshot3.png)




🧮 How It Works

Users enter Location 📍, Area 📐, BHK 🛏, and Bathrooms 🚿.

Inputs are converted into a feature vector for the model.

The ML model predicts the house price.

Predicted price is displayed in lakhs on a Streamlit UI.


