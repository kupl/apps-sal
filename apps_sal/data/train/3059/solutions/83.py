def rain_amount(mm):
    fort = 40 - mm
    fort = str(fort)
    if (mm < 40):
        return "You need to give your plant " + fort + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
