
import streamlit as st
import pandas as pd
from joblib import load

st.set_page_config(page_title="Energy Load Analysis", page_icon="⚡", layout="centered")

MODEL_PATH = "models/decision_tree_model.joblib"
CLASS_NAMES = {
    0: "Normal",
    1: "Low-load shedding",
    2: "Medium-load shedding",
    3: "Critical-load shedding",
}

@st.cache_resource
def get_model():
    return load(MODEL_PATH)

model = get_model()

st.title("⚡ Energy Load Analysis")
st.caption("Decision Tree based load-state classification")

load_ratio = st.slider("Load ratio (%)", 0, 100, 85)
generation_ratio = st.slider("Generation ratio (%)", 0, 100, 50)
battery_soc = st.slider("Battery SOC (%)", 0, 100, 40)
critical_load = st.selectbox("Critical load", ["No", "Yes"])
hour = st.slider("Hour", 0, 23, 12)

row = pd.DataFrame([{
    "load_ratio": load_ratio,
    "generation_ratio": generation_ratio,
    "battery_soc": battery_soc,
    "critical_load": 1 if critical_load == "Yes" else 0,
    "hour": hour,
}])

if st.button("Classify load state"):
    prediction = int(model.predict(row)[0])
    st.success(f"Decision: {CLASS_NAMES[prediction]}")
