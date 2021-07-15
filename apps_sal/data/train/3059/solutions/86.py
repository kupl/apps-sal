def rain_amount(m):
    if(m<40):
        b=40-m
        return "You need to give your plant " + str(b) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"
