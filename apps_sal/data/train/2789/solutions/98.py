def bmi(weight, height):
    stages_of_life = ['Underweight', 'Normal', 'Overweight', 'Obese']
    BMI = weight / height ** 2
    pointer = 0 if BMI <= 18.5 else 1 if BMI <= 25 else 2 if BMI <= 30 else 3
    return stages_of_life[pointer]
