def whoseMove(lastPlayer, win):
    return {
        'black': ['white', 'black'],
        'white': ['black', 'white']
    }.get(lastPlayer)[win]
