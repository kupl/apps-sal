def bmi(weight, height):
    b = weight / (height * height)
    health = {
        18.5: 'Underweight',
        25.0: 'Normal',
        30.0: 'Overweight',
    }
    for i in list(health.keys()):
        if b <= i:
            return health[i]
    return 'Obese'
