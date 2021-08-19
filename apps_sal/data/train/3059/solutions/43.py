def rain_amount(rain_amount):
    if rain_amount < 40:
        return f'You need to give your plant {abs(rain_amount - 40)}mm of water'
    return 'Your plant has had more than enough water for today!'
