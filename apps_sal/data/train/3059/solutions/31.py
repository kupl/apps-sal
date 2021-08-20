def rain_amount(rain):
    if rain < 40:
        return f'You need to give your plant {40 - rain}mm of water'
    else:
        return 'Your plant has had more than enough water for today!'
