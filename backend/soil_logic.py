def calculate_soil_health(nitrogen, phosphorus, potassium, ph, moisture, temperature):
    score = 0

    # Nitrogen: ideal range 20-40
    if 20 <= nitrogen <= 40:
        score += 20
    elif 10 <= nitrogen < 20 or 40 < nitrogen <= 50:
        score += 10

    # Phosphorus: ideal range 15-30
    if 15 <= phosphorus <= 30:
        score += 20
    elif 5 <= phosphorus < 15 or 30 < phosphorus <= 40:
        score += 10

    # Potassium: ideal range 15-30
    if 15 <= potassium <= 30:
        score += 20
    elif 5 <= potassium < 15 or 30 < potassium <= 40:
        score += 10

    # pH: ideal range 6.0-7.5
    if 6.0 <= ph <= 7.5:
        score += 20
    elif 5.0 <= ph < 6.0 or 7.5 < ph <= 8.5:
        score += 10

    # Moisture: ideal range 30-60
    if 30 <= moisture <= 60:
        score += 20
    elif 20 <= moisture < 30 or 60 < moisture <= 70:
        score += 10

    return score