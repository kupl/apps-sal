def a(w, h):
    return w / h ** 2


def bmi(w, h):
    return 'Underweight' if a(w, h) <= 18.5 else 'Normal' if a(w, h) <= 25 else 'Overweight' if a(w, h) <= 30 else 'Obese'
