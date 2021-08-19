def whoseMove(lastPlayer, win):
    lose = {'white': 'black', 'black': 'white'}
    return lastPlayer if win else lose.get(lastPlayer)
