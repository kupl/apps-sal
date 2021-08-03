def rain_amount(rain_amount):
    if rain_amount >= 40:
        return "Your plant has had more than enough water for today!"
    return "You need to give your plant " + str(40 - rain_amount) + "mm of water"
