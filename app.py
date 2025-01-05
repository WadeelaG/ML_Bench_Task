import gradio as gr
from ultralytics import YOLO


model = YOLO("best.onnx")  

def predict_image(img, conf_threshold, iou_threshold):
    
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
    )
    
    return results[0].plot() if results else None


iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Confidence threshold"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="IoU threshold"),
    ],
    outputs=gr.Image(type="pil", label="Result"),
    title="Ultralytics Gradio YOLO Object Detection",
    description="Upload images for YOLO object detection using your custom-trained model.",
)

iface.launch()
