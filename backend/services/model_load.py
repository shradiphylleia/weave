import torch
from transformers import AutoProcessor, AutoModelForVision2Seq

def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    try:
        processor = AutoProcessor.from_pretrained("google/paligemma-3b-mix-224", use_fast=True)
        model = AutoModelForVision2Seq.from_pretrained(
            "google/paligemma-3b-mix-224",
            dtype=torch.bfloat16
        ).to(device)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
        processor, model = None, None

    return model, processor, device
    
