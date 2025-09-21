import torch
from PIL import Image
from io import BytesIO
import base64

def generate_marketing_copy_service(request_data, model, processor, device):

    if request_data.image:
        try:
            image_bytes = base64.b64decode(request_data.image)
            img = Image.open(BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
            return f"Failed to decode image: {e}"
    else:
        img = Image.new("RGB", (224, 224), color=(255, 255, 255))


    prompt_text = (
        "You are a friendly newsletter writer. Create a email to promote brand :\n"        
        "Image product:<image>\n"
    )


    model_inputs = processor(text=prompt_text, images=img, return_tensors="pt").to(device)
    input_len = model_inputs["input_ids"].shape[-1]

    with torch.inference_mode():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=256,
            do_sample=True,
            top_p=0.9,
            temperature=0.7,
            repetition_penalty=1.2
        )

    generated_ids = generated_ids[0][input_len:]  
    marketing_copy = processor.decode(
        generated_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    ).strip()

    return marketing_copy
