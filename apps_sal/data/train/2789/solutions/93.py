def bmi(weight, height):
    bmi_is = weight / (height**2)
    if bmi_is <= 18.5:
        return 'Underweight'
    elif 18.5 < bmi_is <= 25.0:
        return 'Normal'
    elif 25.0 < bmi_is <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
