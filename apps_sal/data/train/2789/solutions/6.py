def bmi(w, h):
    return (lambda b=w / h ** 2: ['Underweight', 'Normal', 'Overweight', 'Obese'][(18.5 < b) + (25 < b) + (30 < b)])()
