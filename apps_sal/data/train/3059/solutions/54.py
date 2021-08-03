def rain_amount(mm):
    remaining_rain = 40 - mm
    if (mm < 40):
        return "You need to give your plant " + str(remaining_rain) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
