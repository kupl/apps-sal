def bmi(weight, height):
    bmeye = weight / height ** 2
    if bmeye <= 18.5:
        return 'Underweight'
    elif bmeye <= 25.0:
        return 'Normal'
    elif bmeye <= 30.0:
        return 'Overweight'
    elif bmeye > 30:
        return 'Obese'
