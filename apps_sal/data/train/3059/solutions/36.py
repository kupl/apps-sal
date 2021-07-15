def rain_amount(mm):
    i = 40
    if (mm < 40):
        i = 40 - mm
        return "You need to give your plant " + str(i) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
