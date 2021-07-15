def rain_amount(mm):
    if 40>mm:
        return "You need to give your plant %imm of water" % (40-mm)
    else:
        return "Your plant has had more than enough water for today!"
