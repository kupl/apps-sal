def rain_amount(amount):
    if amount < 40:
        return "You need to give your plant {}mm of water".format((40 - amount))
    else:
        return "Your plant has had more than enough water for today!"
