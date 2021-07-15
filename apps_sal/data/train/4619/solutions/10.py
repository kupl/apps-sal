def whoseMove(lastPlayer, win):
    return lastPlayer if win else ({'white','black'}-{lastPlayer}).pop()
