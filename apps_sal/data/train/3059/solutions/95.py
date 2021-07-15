def rain_amount(x):
    if x < 40:
         return "You need to give your plant " + str(40-x) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
