def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win:
        return 'black'
    elif lastPlayer == 'white' and win:
        return 'white'
    elif lastPlayer == 'white' and not win:
        return 'black'
    return 'white'
