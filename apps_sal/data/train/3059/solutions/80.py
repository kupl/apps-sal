def rain_amount(x):
    if x > 39:
        return 'Your plant has had more than enough water for today!'
    else:
        return 'You need to give your plant ' + str(40 - x) + 'mm of water'
