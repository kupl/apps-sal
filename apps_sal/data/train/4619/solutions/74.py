def whoseMove(lastPlayer, win):
    if lastPlayer == 'black' and win:
        return 'black'
    if lastPlayer == 'black' and win == False:
        return 'white'
    if lastPlayer == 'white' and win:
        return 'white'
    if lastPlayer == 'white' and win == False:
        return 'black'
