def rain_amount(mm):
    if mm < 40:
        r = 40 - mm
        return "You need to give your plant " + str(r) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
