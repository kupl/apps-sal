def bmi(w, h):
    b = w / (h ** 2)
    if b > 30:
        return "Obese"
    elif b <= 18.5:
        return "Underweight"
    elif b <= 25.0:
        return "Normal"
    elif b <= 30.0:
        return "Overweight"
