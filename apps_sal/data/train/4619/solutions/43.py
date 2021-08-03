def whoseMove(lastPlayer, win):
    if win == False:
        return{'white': 'black', 'black': 'white'}[lastPlayer]
    if win == True:
        return lastPlayer
