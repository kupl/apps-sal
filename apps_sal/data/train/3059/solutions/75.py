def rain_amount(mm):
    rain_amount = 40
    if mm < rain_amount:
        return 'You need to give your plant {}mm of water'.format(rain_amount - mm)
    return 'Your plant has had more than enough water for today!'
