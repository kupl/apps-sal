def bmi(weight, height):
    bmi_1 = weight / height ** 2
    return 'Obese' if bmi_1 > 30 else 'Overweight' if bmi_1 > 25 else 'Normal' if bmi_1 > 18.5 else 'Underweight'
