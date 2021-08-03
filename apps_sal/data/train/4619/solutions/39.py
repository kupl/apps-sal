def whoseMove(lastPlayer, win):
    l = ['black', 'white']
    return lastPlayer if win else l[l.index(lastPlayer) - 1]
