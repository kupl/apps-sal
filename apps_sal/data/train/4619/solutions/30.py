def whoseMove(lastPlayer, win):
    return 'black' if ((lastPlayer == 'black' and win) or (lastPlayer == 'white' and not win)) else 'white'
