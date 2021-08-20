def bmi(weight, height):
    youfat = weight / (height * height)
    if youfat <= 18.5:
        return 'Underweight'
    elif youfat <= 25.0:
        return 'Normal'
    elif youfat <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
