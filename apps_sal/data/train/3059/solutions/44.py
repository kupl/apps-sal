def rain_amount(mm):
    if mm < 40:
        a = 40 - mm
        return 'You need to give your plant {}mm of water'.format(a)
    else:
        return 'Your plant has had more than enough water for today!'
