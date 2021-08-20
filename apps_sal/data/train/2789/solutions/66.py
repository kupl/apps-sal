def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if 18.5 < bmi <= 25.0 else 'Overweight' if 25 < bmi <= 30.0 else 'Obese'
