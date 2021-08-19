def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return 'Underweight'
    if 18.5 < bmi <= 25:
        return 'Normal'
    if 25 < bmi <= 30:
        return 'Overweight'
    if bmi > 30:
        return 'Obese'
