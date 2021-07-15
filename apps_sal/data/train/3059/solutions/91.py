def rain_amount(mm):
    if int(mm) < 40:
         return "You need to give your plant " + str(abs(int(mm) - 40)) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
