def rain_amount(mm):
    if mm >= 40:
        return 'Your plant has had more than enough water for today!'
    else:
        return f'You need to give your plant {abs(mm - 40)}mm of water'
