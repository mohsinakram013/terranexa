def predict_yield(crop, area, soil_health_score, rainfall):
    base_yield_per_hectare = {
        "Wheat": 2.8,
        "Rice": 3.5,
        "Maize": 4.0,
        "Cotton": 1.5
    }

    base = base_yield_per_hectare.get(crop, 2.5)

    soil_factor = soil_health_score / 100
    rainfall_factor = 1.0
    if rainfall < 300:
        rainfall_factor = 0.7
    elif rainfall > 1500:
        rainfall_factor = 0.85

    hectares = area * 0.4047

    estimated_yield_per_hectare = base * soil_factor * rainfall_factor
    total_yield = round(estimated_yield_per_hectare * hectares, 2)

    return {
        "estimated_yield_per_hectare": round(estimated_yield_per_hectare, 2),
        "total_estimated_yield_tons": total_yield,
        "note": "This is an estimate based on average yield data, soil health, and rainfall. Actual yield may vary."
    }