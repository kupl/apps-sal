def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi > 30:
        result = 'Obese'
    elif bmi > 25:
        result = 'Overweight'
    elif bmi > 18.5:
        result = 'Normal'
    else:
        result = 'Underweight'
    return result
