def whoseMove(lastPlayer, win):
    if win == True:
        return lastPlayer
    elif lastPlayer == 'white' and win == False:
        return 'black'
    elif lastPlayer == 'black' and win == False:
        return 'white'
