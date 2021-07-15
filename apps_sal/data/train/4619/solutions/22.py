def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    else:
        if lastPlayer == 'black':
            return 'white'
        else:
            return 'black'
