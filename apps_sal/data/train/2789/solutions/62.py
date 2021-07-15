def bmi(weight, height):
    a = float(weight)
    b = float(height)
    b_m_i = a / b ** 2
    if b_m_i <= 18.5:
        return "Underweight"
    if b_m_i <= 25.0:
        return "Normal"
    if b_m_i <= 30.0:
        return "Overweight"
    if b_m_i > 30:
        return "Obese"
    
    #return "Underweight" if b_m_i <= 18.5 else "Normal" if b_m_i <= 25.0 else "Overweight" if b_m_i <= 30.0  else "Obese" if b_m_i > 30

