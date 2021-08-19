def bmi(weight, height):
    bmi = weight / height ** 2
    print(bmi)
    if bmi <= 18.5:
        result = 'Underweight'
    elif bmi <= 25:
        result = 'Normal'
    elif bmi <= 30:
        result = 'Overweight'
    elif bmi > 30:
        result = 'Obese'
    return result
