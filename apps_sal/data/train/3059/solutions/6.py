def rain_amount(mm):
    if mm >= 40:
        return 'Your plant has had more than enough water for today!'
    return 'You need to give your plant ' + str(40 - mm) + 'mm of water'
