def bmi(weight, height):
    index = weight / (height * height)
    if index <= 18.5:
        return 'Underweight'
    if index <= 25.0:
        return 'Normal'
    if index <= 30.0:
        return 'Overweight'
    if index > 30:
        return 'Obese'
