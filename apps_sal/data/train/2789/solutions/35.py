def bmi(weight, height):
    body = weight / height**2
    if body <= 18.5:
        return "Underweight"
    elif body <= 25.0 and body > 18.5:
        return "Normal"
    elif body <= 30.0 and body > 25:
        return "Overweight"
    else:
        return "Obese"
