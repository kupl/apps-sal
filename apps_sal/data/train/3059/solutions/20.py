def rain_amount(rm):
    if (rm < 40):
        return "You need to give your plant {r}mm of water".format(r=-rm+40)
    else:
        return "Your plant has had more than enough water for today!"
