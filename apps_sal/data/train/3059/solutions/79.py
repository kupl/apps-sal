def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        m = 40 - mm
        return "You need to give your plant " + str(m) + "mm of water"
