a = lambda w, h: w/(h**2)
bmi = lambda w,h: "Underweight" if a(w,h) <= 18.5 else "Normal" if a(w,h) <= 25 else "Overweight" if a(w,h) <= 30 else "Obese"
