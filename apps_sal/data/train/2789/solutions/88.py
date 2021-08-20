def bmi(weight, height):
    score = float(weight / height ** 2.0)
    if score <= 18.5:
        return 'Underweight'
    elif score <= 25.0:
        return 'Normal'
    elif score <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
