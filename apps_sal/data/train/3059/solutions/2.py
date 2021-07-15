def rain_amount(rain_amount):
    if rain_amount < 40:
        return "You need to give your plant " + str(40 - rain_amount) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
