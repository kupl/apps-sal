def whoseMove(lastPlayer, win):
    if win is False:
        if lastPlayer=='black':
            return 'white'
        return 'black'
    if win is True:
        if lastPlayer=='black':
            return 'black'
        return 'white'
