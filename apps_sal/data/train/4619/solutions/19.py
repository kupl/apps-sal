def whoseMove(lastPlayer, win):
    lib = {'white': 'black', 'black':'white'}
    return lastPlayer if win == True else lib[lastPlayer]
