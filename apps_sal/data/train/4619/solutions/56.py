def whoseMove(lastPlayer, win):
    player = {'white': 'black',
             'black': 'white'}
    return lastPlayer if win else player[lastPlayer]
