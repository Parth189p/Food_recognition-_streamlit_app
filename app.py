import streamlit as st
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image
import tempfile
import os

# Must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Food Detection", page_icon="🍛")

# --- Configuration ---
MODEL_PATH = "models/yolov8m-oiv7/weights/best.pt"

# --- Load YOLOv8 Model ---
@st.cache_resource
def load_model():
    """
    Load the YOLOv8 model for food detection.
    """
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model not found at {MODEL_PATH}. Please ensure the path is correct.")
        return None
    return YOLO(MODEL_PATH)

model = load_model()

# --- Streamlit UI Layout ---
st.title("🍛 Food Detection with YOLOv8")
st.caption("Upload a food image to see detected items using a fine-tuned YOLOv8 model.")

# --- Image Upload ---
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png", "bmp", "webp"],
    help="Upload a food image (jpg, jpeg, png, bmp, webp) for object detection."
)

if uploaded_file is not None:
    try:
        img_pil = Image.open(uploaded_file).convert("RGB")
        img_np = np.array(img_pil)

        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.image(img_np, caption="Uploaded Image", use_container_width=False, width=800)

        if model:
            # Save temporarily
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmpfile:
                img_pil.save(tmpfile.name)
                temp_img_path = tmpfile.name

            # Inference
            with st.spinner("Running detection..."):
                results = model.predict(source=temp_img_path, save=False, show=False)

            for r in results:
                annotated_img = r.plot()
                # Convert BGR to RGB
                annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

            with col2:
                st.image(annotated_img, caption="🔍 Detected Objects", use_container_width=False, width=800)

                # Optional download
                output_path = os.path.join("outputs", f"annotated_{uploaded_file.name}")
                os.makedirs("outputs", exist_ok=True)
                cv2.imwrite(output_path, annotated_img)

                with open(output_path, "rb") as f:
                    st.download_button(
                        "📥 Download Annotated Image",
                        f,
                        file_name=f"annotated_{uploaded_file.name}",
                        mime="image/jpeg"
                    )
        else:
            st.error("Model failed to load.")
    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")
else:
    st.info("Please upload a food image to begin detection.")

st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit and YOLOv8")
