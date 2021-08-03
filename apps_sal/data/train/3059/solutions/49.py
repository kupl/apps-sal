def rain_amount(mm):
    f = str(40 - mm)
    c = "You need to give your plant "
    d = "mm of water"
    if mm <= 39:
        return c + f + d
    else:
        return "Your plant has had more than enough water for today!"
