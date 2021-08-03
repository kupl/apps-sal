def whoseMove(lastPlayer, win):
    if lastPlayer == "black":
        return lastPlayer if win else 'white'
    else:
        return 'white' if win else 'black'
