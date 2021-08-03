def bmi(weight, height):
    i = weight / height**2
    return 'Underweight' if i <= 18.5 else 'Normal' if i <= 25 else 'Overweight' if i <= 30 else 'Obese'
