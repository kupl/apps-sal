def bmi(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <= 18.5:
        output = 'Underweight'
    elif bmi <= 25:
        output = 'Normal'
    elif bmi <= 30:
        output = 'Overweight'
    else:
        output = 'Obese'
    return output
