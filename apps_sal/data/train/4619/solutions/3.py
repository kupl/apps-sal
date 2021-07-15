def whoseMove(lastPlayer, win):
    return ['black', 'white'][(lastPlayer == 'black') ^ win]
