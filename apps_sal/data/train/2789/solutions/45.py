def bmi(weight, height):
    a = weight / height ** 2
    if a <= 18.5:
        return "Underweight"
    elif a <= 25.0:
        return "Normal"
    elif a <= 30.0:
        return "Overweight"
    return "Obese"
