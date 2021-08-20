def bmi(w, h):
    return next((s for (s, t) in zip('Obese Overweight Normal Underweight'.split(), (30, 25, 18.5, 0)) if w / h / h > t))
