def bmi(weight, height):
    BMI = float(weight) / float(height ** 2)
    if BMI <= 18.5:
        return 'Underweight'
    elif BMI <= 25.0:
        return 'Normal'
    elif BMI <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
