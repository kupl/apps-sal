def whoseMove(lastPlayer, win):
    if lastPlayer == 'black':
        return 'white' if win == False else 'black'
    elif lastPlayer == 'white':
        return 'black' if win == False else 'white'
