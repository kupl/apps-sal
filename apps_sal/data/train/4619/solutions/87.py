def whoseMove(lastPlayer, win):
    return "white" if ("white" == lastPlayer and win == True) or (lastPlayer == "black" and win == False) else "black"
