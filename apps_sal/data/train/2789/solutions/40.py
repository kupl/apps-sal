def bmi(weight, height):
    bm = weight / (height**2)
    if bm <= 18.5:
        return "Underweight"
    if bm <= 25.0:
        return "Normal"
    if bm <= 30.0:
        return "Overweight"
    return "Obese"
