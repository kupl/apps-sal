def whoseMove(lastPlayer, win):
    p = {'black': 'white', 'white': 'black'}
    if win:
        return lastPlayer
    else:
        return p[lastPlayer]
