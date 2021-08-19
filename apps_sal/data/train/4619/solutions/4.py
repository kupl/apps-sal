def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        if win == True:
            return 'black'
        else:
            return 'white'
    elif win == True:
        return 'white'
    else:
        return 'black'
