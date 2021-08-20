def bmi(weight, height):
    bmi = weight / pow(height, 2)
    if bmi > 30:
        result = 'Obese'
    elif bmi <= 30.0 and bmi > 25.0:
        result = 'Overweight'
    elif bmi <= 25.0 and bmi > 18.5:
        result = 'Normal'
    else:
        result = 'Underweight'
    return result
