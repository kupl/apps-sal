def bmi(weight, height):
    abmi = weight / (height * height)
    if abmi <= 18.5:
        return "Underweight"
    elif 18.5 < abmi <= 25.0:
        return "Normal"
    elif 25.0 < abmi <= 30.0:
        return "Overweight"
    elif 30.0 < abmi:
        return "Obese"
    # your code here
