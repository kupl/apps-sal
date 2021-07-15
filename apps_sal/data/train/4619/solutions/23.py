def whoseMove(p, win):
    return p if win else ['white', 'black'][p == 'white']
