def bmi(w, h):
    return "Underweight" if w/(h**2)<=18.5 else "Normal" if w/(h**2)<=25 else "Overweight" if w/(h**2)<=30 else "Obese"
