def bmi(w, h): return (lambda x: 'Underweight' if x <= 18.5 else 'Normal' if x <= 25 else 'Overweight' if x <= 30 else 'Obese')(w / h**2)
