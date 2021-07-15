def bmi(weight, height):
    x = weight / height ** 2
    return "Obese" if x > 30 else "Overweight" if x > 25 else "Normal" if x > 18.5 else "Underweight"
