def bmi(weight, height):
    bmi_x = weight / height**2
    if bmi_x <= 18.5:
        return "Underweight";
    elif bmi_x <= 25.0:
        return "Normal";
    elif bmi_x <= 30.0:
        return "Overweight";
    else:
        return "Obese";
