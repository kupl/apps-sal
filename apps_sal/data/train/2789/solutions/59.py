def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        resultato = 'Underweight'
    elif bmi <= 25:
        resultato = 'Normal'
    elif bmi <= 30:
        resultato = 'Overweight'
    else:
        resultato = 'Obese'
    return resultato
