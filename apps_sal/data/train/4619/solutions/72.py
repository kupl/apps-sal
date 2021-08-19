def whoseMove(lastPlayer, win):
    if win == True:
        return lastPlayer
    else:
        return 'black' if lastPlayer == 'white' and win == False else 'white'
