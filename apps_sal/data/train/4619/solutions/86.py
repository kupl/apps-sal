def whoseMove(lastPlayer, win):
    if lastPlayer == 'white' and win is True:
        return 'white'
    if lastPlayer == 'black' and win is True:
        return 'black'
    if lastPlayer == 'white' and win is False:
        return 'black'
    if lastPlayer == 'black' and win is False:
        return 'white'
