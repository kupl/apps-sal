def bmi(weight, height):
    calculation =weight/height**2
    if calculation <=18.5:
        return 'Underweight'
    if calculation <= 25.0:
        return 'Normal'
    if calculation <= 30.0:
        return 'Overweight'
    if calculation > 30:
        return 'Obese'
