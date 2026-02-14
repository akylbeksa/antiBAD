import gradio as gr
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/YOLOv8_Small_RDD.pt")
model = YOLO(MODEL_PATH)

def predict(img: Image.Image):
    img = img.convert("RGB")
    res = model.predict(np.array(img), conf=0.25, verbose=False)[0]
    out = Image.fromarray(res.plot()[..., ::-1])
    return out

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload road image"),
    outputs=gr.Image(type="pil", label="Detections"),
    title="antiBAD — Road Damage Detection Demo",
)

demo.launch()
