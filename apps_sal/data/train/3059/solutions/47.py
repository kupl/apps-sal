def rain_amount(mm):       
    s1 = "Your plant has had more than enough water for today!"
    return s1 if mm >= 40 else  f"You need to give your plant {40 - mm}mm of water"
