def rain_amount(water):
    if water < 40:
        return 'You need to give your plant ' + str(40 - water) + 'mm of water'
    else:
        return 'Your plant has had more than enough water for today!'
