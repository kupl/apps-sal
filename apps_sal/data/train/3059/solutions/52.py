def rain_amount(rain_amount):
    if rain_amount < 40:
        water = 40 - rain_amount
        return 'You need to give your plant ' + str(water) + 'mm of water'
    else:
        return 'Your plant has had more than enough water for today!'
