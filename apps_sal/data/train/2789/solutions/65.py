def bmi(weight, height):
    b = weight/height/height
    if b <= 18.5: return 'Underweight'
    if b <= 25: return 'Normal'
    if b <= 30: return 'Overweight'
    return 'Obese'
