def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        return ['black', 'white'][not win]
    return ['black', 'white'][win]
