def bmi(weight, height):

    bmi = weight * 10 // (height**2)

    if bmi in range(185):
        return 'Underweight'
    elif bmi in range(185, 250):
        return 'Normal'
    elif bmi in range(250, 300):
        return 'Overweight'
    elif bmi > 300:
        return 'Obese'
