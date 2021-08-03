def whoseMove(lastPlayer, win):
    voc = {'black': 'white', 'white': 'black'}
    if win:
        return lastPlayer
    else:
        return voc[lastPlayer]
