def whoseMove(lastPlayer, win):
    temp = {'black': 'white', 'white': 'black'}
    if win == True:
        return lastPlayer
    else:
        return temp[lastPlayer]
