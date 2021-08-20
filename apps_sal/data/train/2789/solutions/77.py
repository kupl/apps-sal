def bmi(w, h):
    p = round(w // h // h, 1)
    return 'Underweight' if p <= 18.5 else 'Normal' if p <= 25.0 else 'Overweight' if p <= 30 else 'Obese'
