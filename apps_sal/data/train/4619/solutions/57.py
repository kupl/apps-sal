def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        nextPlayer = 'white'
    else:
        nextPlayer = 'black'
    if win:
        return lastPlayer
    else:
        return nextPlayer
