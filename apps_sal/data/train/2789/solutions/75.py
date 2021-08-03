def bmi(w, h):
    b = w / (h * h)
    if b <= 18.5:
        return "Underweight"
    if b <= 25.0:
        return "Normal"
    if b <= 30.0:
        return "Overweight"
    if b > 30:
        return "Obese"
