def whoseMove(lastPlayer, win):
    if lastPlayer=="black" and win or lastPlayer=="white" and not(win):
        return "black"
    if lastPlayer=="white" and win or lastPlayer=="black" and not(win):
        return "white"

