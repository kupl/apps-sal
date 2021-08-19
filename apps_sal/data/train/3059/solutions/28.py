def rain_amount(mm):
    r = str(40 - mm)
    if mm < 40:
        return 'You need to give your plant ' + r + 'mm of water'
    else:
        return 'Your plant has had more than enough water for today!'
