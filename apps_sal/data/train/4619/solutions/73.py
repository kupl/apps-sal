def whoseMove(lastPlayer, win):
    pls = ['black', 'white']
    return lastPlayer if win else pls[pls.index(lastPlayer) - 1]
