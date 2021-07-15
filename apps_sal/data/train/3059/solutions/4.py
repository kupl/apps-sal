def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        return "You need to give your plant %smm of water" % (40 - mm)
