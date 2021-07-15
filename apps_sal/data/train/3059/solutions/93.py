def rain_amount(rain):
    if rain >= 40:
         return "Your plant has had more than enough water for today!"    
    else:
         return "You need to give your plant {}mm of water".format(40-rain)


