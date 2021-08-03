def bmi(w, h): return (lambda b: "Underweight" if b <= 18.5 else "Normal" if b <= 25.0 else "Overweight" if b <= 30.0 else "Obese")(w / h / h)
