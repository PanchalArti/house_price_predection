import streamlit as st
import pickle
import json
import numpy as np
import os
import time

# ------------------ Load Model & Columns ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "home_prices_pred_model.pickle"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "columns.json"), "r") as f:
    data_columns = json.load(f)["data_columns"]

locations = sorted([c for c in data_columns if c not in ["total_sqft", "bath", "bhk"]])

# ------------------ Prediction Function ------------------
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(data_columns))
    x[data_columns.index("total_sqft")] = sqft
    x[data_columns.index("bath")] = bath
    x[data_columns.index("bhk")] = bhk

    if location in data_columns:
        x[data_columns.index(location)] = 1

    return round(model.predict([x])[0], 2)

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1572120360610-d971b9a0e42e");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main container overlay */
    .main {
        background-color: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 15px;
    }

    /* Title styling */
    h1 {
        font-size: 80px !important;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }

    p.subtitle {
        text-align: center;
        color: white;
        font-size: 32px;
        margin-top: 5px;
    }

    /* Prediction result box */
    .result {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 40px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 30px;
        margin-top: 20px;
    }

    .result h2 {
        font-size: 50px !important;
        margin-bottom: 15px;
    }

    /* Metrics */
    .stMetricValue {
        font-size: 32px !important;
    }

    .stMetricLabel {
        font-size: 22px !important;
    }

    /* Sidebar heading */
    .css-1d391kg {
        font-size: 50px !important;
        font-weight: bold;
        background: linear-gradient(to right, yellow, green, blue);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Sidebar labels */
    .css-1aumxhk, .css-1fv8s86 { 
        font-size: 24px !important;
        color: white;
    }

    /* Slider value text */
    .css-1v3fvcr { 
        font-size: 22px !important;
        color: white;
    }

    /* Sidebar container overlay */
    .css-1d391kg + div { 
        background-color: rgba(0,0,0,0.6);
        border-radius: 15px;
        padding: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: lightgray;
        font-size: 18px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Header ------------------
st.markdown("<h1>🏡 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict home prices instantly using Machine Learning</p>", unsafe_allow_html=True)
st.divider()

# ------------------ Sidebar ------------------
st.sidebar.title("🔧 Enter Property Details")

location = st.sidebar.selectbox("📍 Location", locations)
sqft = st.sidebar.slider("📐 Total Area (sqft)", 300, 5000, 1000, step=50)
bhk = st.sidebar.selectbox("🛏 BHK", [1, 2, 3, 4, 5])
bath = st.sidebar.selectbox("🚿 Bathrooms", [1, 2, 3, 4, 5])

# ------------------ Metrics ------------------
col1, col2 = st.columns(2)
with col1:
    st.metric("📐 Area (sqft)", sqft)
with col2:
    st.metric("🛏 BHK / 🚿 Bath", f"{bhk} / {bath}")

st.divider()

# ------------------ Predict Button ------------------
if st.button("🔮 Predict Price", use_container_width=True):
    with st.spinner("Predicting house price..."):
        time.sleep(1)
        price = predict_price(location, sqft, bath, bhk)

    st.success("Prediction Successful 🎉")

    st.markdown(
        f"""
        <div class="result">
            <h2>₹ {price} Lakhs</h2>
            <p><b>Location:</b> {location}</p>
            <p><b>Area:</b> {sqft} sqft</p>
            <p><b>BHK:</b> {bhk} | <b>Bath:</b> {bath}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------ Footer ------------------
st.markdown("<div class='footer'>Built by Arti Panchal </div>", unsafe_allow_html=True)
