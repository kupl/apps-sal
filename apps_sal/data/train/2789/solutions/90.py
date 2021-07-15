def bmi(weight, height):
    bmi = weight / height ** 2
    
    if bmi <= 18.5:
        r = "Underweight"
    elif bmi <= 25:
        r = "Normal"
    elif bmi <= 30:
        r = "Overweight"
    else:
        r = "Obese"
    return r
