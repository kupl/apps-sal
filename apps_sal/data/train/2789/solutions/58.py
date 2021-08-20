def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        risultato = 'Underweight'
    elif bmi <= 25.0:
        risultato = 'Normal'
    elif bmi <= 30.0:
        risultato = 'Overweight'
    else:
        risultato = 'Obese'
    return risultato
