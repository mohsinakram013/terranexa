from PIL import Image

def analyze_leaf_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((100, 100))

    pixels = list(img.getdata())
    total_pixels = len(pixels)

    r_avg = sum(p[0] for p in pixels) / total_pixels
    g_avg = sum(p[1] for p in pixels) / total_pixels
    b_avg = sum(p[2] for p in pixels) / total_pixels

    if g_avg > r_avg and g_avg > b_avg:
        result = "Healthy"
        confidence = round((g_avg / 255) * 100, 2)
        advice = "No signs of disease detected. Continue regular monitoring."
    elif r_avg > g_avg and r_avg > b_avg:
        result = "Possible Leaf Blight"
        confidence = round((r_avg / 255) * 100, 2)
        advice = "Reddish/brown discoloration detected. Consult an agriculture expert and consider fungicide treatment."
    else:
        result = "Possible Nutrient Deficiency"
        confidence = round((g_avg / 255) * 100, 2)
        advice = "Yellowing detected, which may indicate nitrogen deficiency. Consider soil testing."

    return {
        "result": result,
        "confidence": confidence,
        "advice": advice,
        "note": "This is an AI-assisted preliminary detection, not a guaranteed diagnosis. Please consult an agriculture expert for confirmation."
    }uvicorn main:app --reload