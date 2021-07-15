def bmi(w, h):
    if w/h**2 <=18.5:
        return 'Underweight'
    elif w/h**2 <=25.0:
        return 'Normal'
    elif w/h**2 <=30.0:
        return 'Overweight'
    elif w/h**2 >30:
        return 'Obese'
