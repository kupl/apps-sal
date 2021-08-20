def bmi(weight, height):
    text = ['Overweight', 'Normal', 'Underweight', 'Obese']
    bmi = weight / height ** 2
    print(bmi)
    index = bool(bmi <= 18.5) + bool(bmi <= 25) + bool(bmi <= 30)
    print(bool(bmi <= 18.5), bool(bmi <= 25), bool(bmi <= 30), bool(bmi > 30))
    print(index)
    return text[index - 1]
