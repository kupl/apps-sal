def whoseMove(lastPlayer, win):
    if win and lastPlayer == 'black': return 'black'
    if not(win) and lastPlayer == 'white': return 'black'
    return 'white'

