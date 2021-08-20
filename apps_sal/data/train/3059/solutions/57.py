def rain_amount(mm):
    needed_watering = 40 - mm
    if mm < 40:
        return 'You need to give your plant {}mm of water'.format(needed_watering)
    else:
        return 'Your plant has had more than enough water for today!'
