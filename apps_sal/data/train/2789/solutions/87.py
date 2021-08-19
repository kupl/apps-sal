def bmi(weight, height):
    are_you_fat = weight / height ** 2
    if are_you_fat <= 18.5:
        return 'Underweight'
    elif are_you_fat <= 25.0 and are_you_fat > 18.5:
        return 'Normal'
    elif are_you_fat <= 30.0 and are_you_fat > 25.0:
        return 'Overweight'
    else:
        return 'Obese'
