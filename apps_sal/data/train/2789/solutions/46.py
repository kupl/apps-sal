def bmi(weight, height):
    index = weight / height**2
    if index > 30:
        return "Obese"
    elif index > 25:
        return "Overweight"
    elif index > 18.5:
        return "Normal"
    else:
        return "Underweight"
