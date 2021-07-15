def bmi(weight, height):
    bmi = weight / height**2
    return ["Obese", "Overweight", "Normal", "Underweight"][(bmi<=30) + (bmi<=25) + (bmi<=18.5)]
