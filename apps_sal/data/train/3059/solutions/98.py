def rain_amount(mm, needs=40):
    water_amount = needs - mm
    if water_amount > 0:
        return "You need to give your plant " + str(water_amount) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
