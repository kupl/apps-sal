def bmi(weight, height):
    bmi_res = weight / height ** 2
    if bmi_res <= 18.5:
        return 'Underweight'
    elif bmi_res <= 25:
        return 'Normal'
    elif bmi_res <= 30:
        return 'Overweight'
    else:
        return 'Obese'
