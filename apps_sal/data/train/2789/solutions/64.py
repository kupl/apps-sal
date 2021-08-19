def bmi(weight, height):
    bmi = weight / (height * height)
    result = ''
    if bmi <= 18.5:
        result = 'Underweight'
    elif bmi <= 25.0:
        result = 'Normal'
    elif bmi < 30.0:
        result = 'Overweight'
    elif bmi > 30:
        result = 'Obese'
    return result
