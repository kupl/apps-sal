def bmi(weight, height):
    a = weight / height ** 2
    if (a > 30):
        return 'Obese'
    if a >= 25:
        return 'Overweight'
    if a >= 18.5:
        return 'Normal'
    return 'Underweight'
