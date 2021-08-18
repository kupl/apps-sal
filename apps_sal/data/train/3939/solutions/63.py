def rps(p1, p2):
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if rules.get(p1) == p2:
        a = 1
    elif rules.get(p2) == p1:
        a = 2
    else:
        return 'Draw!'

    return f'Player {a} won!'
