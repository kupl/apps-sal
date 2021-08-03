def whoseMove(lastPlayer, win):
    d = {'black': 'white', 'white': 'black'}
    if win:
        return lastPlayer
    else:
        return d[lastPlayer]
