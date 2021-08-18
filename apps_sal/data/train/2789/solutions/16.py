def bmi(weight, height):
    BMI = weight / (height**2)
    if BMI > 30:
        return 'Obese'
    elif BMI > 25:
        return 'Overweight'
    elif BMI > 18.5:
        return 'Normal'
    else:
        return 'Underweight'
