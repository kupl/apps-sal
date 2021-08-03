def rain_amount(mm):
    if (40 - mm > 0):
        return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
