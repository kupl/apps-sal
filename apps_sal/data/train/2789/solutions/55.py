def bmi(weight, height):
    bmi_i = weight / height ** 2
    if bmi_i <= 18.8:
        return "Underweight" 
    if bmi_i <= 25.0:
        return "Normal"
    if bmi_i <= 30.0:
        return "Overweight" 
    if bmi_i > 30:
        return "Obese"
