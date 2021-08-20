def bmi(weight, height):
    bmi_score = weight / height ** 2
    print(bmi_score)
    if bmi_score <= 18.5:
        return 'Underweight'
    elif bmi_score <= 25.0:
        return 'Normal'
    elif bmi_score <= 30:
        return 'Overweight'
    else:
        return 'Obese'
