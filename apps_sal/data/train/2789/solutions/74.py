def bmi(weight, height):
    beem = round(weight / height ** 2, 1)
    print(beem)
    if 18.5 >= beem:
        return 'Underweight'
    elif 25.0 >= beem > 18.5:
        return 'Normal'
    elif 30.0 >= beem > 18.5:
        return 'Overweight'
    else:
        return 'Obese'
