def bmi(w, h):
    bmi = w / h ** 2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25:
        return 'Normal'
    elif bmi <= 30:
        return 'Overweight'
    else:
        return 'Obese'
