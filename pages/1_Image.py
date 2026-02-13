import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("antiBAD — Image Demo")

@st.cache_resource
def load_model():
    return YOLO("models/YOLOv8_Small_RDD.pt")  # <-- поменяй на твой .pt

model = load_model()

uploaded = st.file_uploader("Upload a road image", type=["jpg","jpeg","png"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Input", use_column_width=True)

    res = model.predict(np.array(img), conf=0.25)[0]
    st.image(res.plot(), caption="Detections", use_column_width=True)
