def bmi(weight, height):
    bmi = weight / height ** 2
    res = None
    if bmi <= 18.5:
        res = "Underweight"
    elif bmi <= 25:
        res = 'Normal'
    elif bmi <= 30:
        res = 'Overweight'
    else:
        res = 'Obese'
    return res
