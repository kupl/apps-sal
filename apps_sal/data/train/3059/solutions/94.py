def rain_amount(rain):
    print(rain)
    if rain >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        return "You need to give your plant " + str(40-rain) + "mm of water"

