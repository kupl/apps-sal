def bmi(weight, height):
    c = (weight / height**2)
    if(c <= 18.5):
        return "Underweight"
    elif(c <= 25.0):
        return "Normal"
    elif(c <= 30.0):
        return "Overweight"
    return "Obese"
