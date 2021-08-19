def bmi(w, h):
    x = w / h ** 2
    if x <= 18.5:
        return 'Underweight'
    elif 18.5 < x <= 25.0:
        return 'Normal'
    elif 25.0 < x <= 30.0:
        return 'Overweight'
    elif x > 30.0:
        return 'Obese'
