import gradio as gr
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/YOLOv8_Small_RDD.pt")  # <-- поменяй на свой путь

model = YOLO(MODEL_PATH)

def predict(img: Image.Image):
    img = img.convert("RGB")
    res = model.predict(np.array(img), conf=0.25, verbose=False)[0]
    out = Image.fromarray(res.plot()[..., ::-1])  # res.plot() часто BGR
    return out

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload road image"),
    outputs=gr.Image(type="pil", label="Detections"),
    title="antiBAD — Road Damage Detection Demo",
    description="Upload an image of a road. The model will detect potholes/cracks and draw bounding boxes."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", "7860")))
