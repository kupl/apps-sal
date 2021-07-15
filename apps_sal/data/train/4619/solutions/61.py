def whoseMove(lastPlayer, win):
    if lastPlayer=='black':
        return 'black' if win == True else 'white'
    else:
        return 'white' if win == True else 'black'
