def bmi(weight, height):
    bmi = weight / height ** 2
    arr = 'Underweight Normal Overweight Obese'.split()
    return arr[(bmi > 18.5) + (bmi > 25) + (bmi > 30)]
