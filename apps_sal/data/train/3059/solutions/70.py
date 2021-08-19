def rain_amount(mm):
    if mm < 40:
        return 'You need to give your plant {:d}mm of water'.format(40 - mm)
    else:
        return 'Your plant has had more than enough water for today!'
