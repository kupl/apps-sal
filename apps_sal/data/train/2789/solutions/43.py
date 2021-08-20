def bmi(weight, height):
    bmi = weight / height ** 2
    for (i, limit) in enumerate((18.5, 25, 30)):
        if bmi <= limit:
            return ('Underweight', 'Normal', 'Overweight')[i]
    else:
        return 'Obese'
