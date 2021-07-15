def bmi(weight, height):
    f = (weight / height)/ height
    if f <= 18.5:
        return "Underweight"
    elif f <= 25.0:
        return "Normal"
    elif f <= 30.0:
        return "Overweight"
    elif f > 30:
        return "Obese"
