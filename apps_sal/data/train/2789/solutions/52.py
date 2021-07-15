def bmi(weight, height):
    bmi = weight / pow(height, 2)
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi > 18.5) + (bmi > 25.0) + (bmi > 30)]
