def whoseMove(lastPlayer, win):
    if win == False and lastPlayer == 'black':
        return 'white'
    elif win == False and lastPlayer == 'white':
        return 'black'
    return lastPlayer
