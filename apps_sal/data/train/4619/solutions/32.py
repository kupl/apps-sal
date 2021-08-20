def whoseMove(lastPlayer, win):
    d = {'black': 'white', 'white': 'black'}
    return lastPlayer if win else d.get(lastPlayer)
