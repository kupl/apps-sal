def rain_amount(mm):
    if mm < 40:
        return "You need to give your plant " + "{}".format(40 - mm) + "mm of water"
    elif mm >= 40:
         return "Your plant has had more than enough water for today!"
