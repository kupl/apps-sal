def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    elif lastPlayer == 'black':
        return 'white'
    else:
        return 'black'
