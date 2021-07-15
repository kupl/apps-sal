def bmi(weight, height):
    bmi = weight / (height*height)
    return "Underweight" if bmi <= 18.5 else("Normal" if bmi <= 25.0 else("Overweight" if bmi <= 30 else "Obese")) 
