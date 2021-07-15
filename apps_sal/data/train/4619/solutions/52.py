def whoseMove(lastPlayer, win):
    a = ['black','white']
    return lastPlayer if win else a[(a.index(lastPlayer)+1)%2]
