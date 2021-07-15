def hydrate(drinks):
    water = sum([int(drink) for drink in drinks if drink.isnumeric()])
    return '1 glass of water' if water == 1 else '%d glasses of water' % water
