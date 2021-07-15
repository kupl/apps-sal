def calculate_1RM(w, r):
    if r == 0: return 0
    if r == 1: return w
    
    return round(max([
      w * (1 + r / 30),                 # Epley
      100 * w / (101.3 - 2.67123 * r),  # McGlothin
      w * r**0.10                       # Lombardi
      ]))
