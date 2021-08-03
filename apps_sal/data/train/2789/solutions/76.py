def bmi(weight, height):
    b = weight / (height**2)
    if b > 30:
        return 'Obese'
    else:
        if b <= 25:
            if b <= 18.5:
                return 'Underweight'
            else:
                return 'Normal'
        else:
            return 'Overweight'
