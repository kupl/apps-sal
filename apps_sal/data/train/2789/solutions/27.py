def bmi(w, h): return (lambda x: [[["Underweight", "Normal"][18.5 < x <= 25], "Overweight"][25 < x <= 30], "Obese"][x > 30])(w / h**2)
