def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        return 'black' if win else 'white'
    else:
        return 'white' if win else 'black'
