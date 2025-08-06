import requests

def generate_image(prompt, name):
    url = "https://api.example.com/generate"  # Replace with actual API endpoint
    payload = {
        "model": "dall-e-mini",
        "prompt": prompt,
        "name": name
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        image_url = response.json().get("image_url")
        print(f"Beautiful bird image for {name}: {image_url}")
    else:
        print(f"Oops! Couldn't generate bird image for {name}. Error: {response.status_code}")

prompt = "A flock of colorful birds flying over a golden sunset"
name = "Aakarshi"
generate_image(prompt, name)
