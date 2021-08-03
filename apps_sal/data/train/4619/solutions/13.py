def whoseMove(lastPlayer, win):
    return lastPlayer if win else {'white': 'black', 'black': 'white'}.get(lastPlayer)
