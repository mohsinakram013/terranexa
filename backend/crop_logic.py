def recommend_crops(nitrogen, phosphorus, potassium, ph, temperature, humidity, rainfall):
    crops = []

    # Wheat
    wheat_score = 0
    if 20 <= nitrogen <= 40: wheat_score += 25
    if 6.0 <= ph <= 7.5: wheat_score += 25
    if 10 <= temperature <= 25: wheat_score += 25
    if 300 <= rainfall <= 800: wheat_score += 25
    crops.append({"crop": "Wheat", "suitability": wheat_score})

    # Rice
    rice_score = 0
    if 30 <= nitrogen <= 60: rice_score += 25
    if 5.5 <= ph <= 6.5: rice_score += 25
    if 20 <= temperature <= 35: rice_score += 25
    if 1000 <= rainfall <= 2000: rice_score += 25
    crops.append({"crop": "Rice", "suitability": rice_score})

    # Maize
    maize_score = 0
    if 25 <= nitrogen <= 50: maize_score += 25
    if 5.5 <= ph <= 7.0: maize_score += 25
    if 18 <= temperature <= 27: maize_score += 25
    if 500 <= rainfall <= 1000: maize_score += 25
    crops.append({"crop": "Maize", "suitability": maize_score})

    # Cotton
    cotton_score = 0
    if 20 <= nitrogen <= 40: cotton_score += 25
    if 6.0 <= ph <= 8.0: cotton_score += 25
    if 25 <= temperature <= 35: cotton_score += 25
    if 500 <= rainfall <= 1000: cotton_score += 25
    crops.append({"crop": "Cotton", "suitability": cotton_score})

    crops.sort(key=lambda x: x["suitability"], reverse=True)
    return crops