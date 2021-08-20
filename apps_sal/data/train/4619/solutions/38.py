def whoseMove(lastPlayer, win):
    if lastPlayer == 'white':
        opp = 'black'
    else:
        opp = 'white'
    return lastPlayer if win else opp
