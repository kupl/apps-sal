def whoseMove(last, win):
    return last if win else {'white': 'black', 'black': 'white'}[last]
