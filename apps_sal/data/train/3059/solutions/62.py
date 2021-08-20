def rain_amount(mm):
    if mm >= 40:
        return 'Your plant has had more than enough water for today!'
    if mm is not 40:
        remaining = 40 - int(mm)
        return 'You need to give your plant {}mm of water'.format(remaining)
