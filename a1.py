"""
Text-to-Image Generator - Student Template

INSTALL: pip install huggingface-hub pillow
"""
from huggingface_hub import InferenceClient
import requests
from datetime import datetime
from PIL import Image
from config import HF_API_KEY

MODELS = [

    "ByteDance/SDXL-lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5",
]

client = InferenceClient(api_key = HF_API_KEY)

print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")


while True:

    prompt = input("Enter prompt:").strip()

    if prompt.lower() in ["quit", "q", "exit"]:

        break

    if not prompt:

        continue

    print("Generating image...")

    image = None

    for model in MODELS:

        try:

            image = client.text_to_image(prompt, model = model)

            break

        except Exception:

            print(f"Executing model...")

            continue

    if image:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        image.save(filename)
        print(f"Saved {filename}")
        image.show()
        print()
    else:
        print("Error! All models failed. Check you API key\n")


print("Goodbye!")


