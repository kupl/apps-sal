def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    elif not win:
        if lastPlayer == 'black':
            return 'white'
        else:
            return 'black'
