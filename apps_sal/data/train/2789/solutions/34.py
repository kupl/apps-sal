def bmi(weight, height):
    bmi = round(weight / height**2, 1)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
