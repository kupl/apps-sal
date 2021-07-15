def whoseMove(lastPlayer, win):
    if win != True:
        if lastPlayer == 'black':
            return 'white'
        else:
            return 'black'
    else:
        return lastPlayer
