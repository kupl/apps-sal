def whoseMove(lastPlayer, win):
    if win and lastPlayer == 'black':
        return 'black'
    elif win and lastPlayer == 'white':
        return 'white'
    elif not win and lastPlayer == 'black':
        return 'white'
    else:
        return 'black'
