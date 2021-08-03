def bmi(w, h):
    s = w / h ** 2
    if s <= 18.5:
        return "Underweight"
    if s <= 25:
        return "Normal"
    if s <= 30:
        return "Overweight"
    return "Obese"
