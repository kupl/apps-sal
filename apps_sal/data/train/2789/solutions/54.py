def bmi(weight, height):
    body = weight / height ** 2
    if body <= 18.5:
        return "Underweight"
    elif body <= 25.0:
        return "Normal"
    elif body <= 30.0:
        return "Overweight"
    elif body > 30:
        return "Obese"
