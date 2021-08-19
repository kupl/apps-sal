def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win is False:
        return 'white'
    elif lastPlayer == 'black' and win is True:
        return 'black'
    elif lastPlayer == 'white' and win is False:
        return 'black'
    elif lastPlayer == 'white' and win is True:
        return 'white'
