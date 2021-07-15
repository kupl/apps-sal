def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        if win == True:
            return 'black'
        else:
            return 'white'
    else:
        if win == True:
            return 'white'
        else:
            return 'black'
