def bmi(weight, height):
    bmi = weight / height ** 2
    return (["Underweight", "Normal", "Overweight", "Obese"]
            [int(bmi > 18.5) + int(bmi > 25.0) + int(bmi > 30.0)])
