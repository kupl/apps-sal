def rain_amount(mm):
    cat = 40 - mm
    dog = str(cat)
    if mm < 40:
        return "You need to give your plant " + dog + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"
