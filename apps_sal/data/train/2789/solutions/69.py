def bmi(weight, height):
    b = (weight / (height**2))
    if(b <= 18.5):
        return "Underweight"
    elif(18.5 < b <= 25.0):
        return "Normal"
    elif(25.0 < b <= 30.0):
        return "Overweight"
    else:
        return "Obese"
