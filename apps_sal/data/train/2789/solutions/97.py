def bmi(weight, height):
    body_mass = weight / height**2
    result = ""
    if body_mass <= 18.5:
        result = "Underweight"
    elif body_mass <= 25.0:
        result = "Normal"
    elif body_mass <= 30.0:
        result = "Overweight"
    else:
        result = "Obese"
    return result
