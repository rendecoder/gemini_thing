model = genai.GenerativeModel(model_name="gemini-pro-vision")

response = model.generate_content(["What’s in this photo?", img])