def whoseMove(lastPlayer, win):
    return ["white", "black"][(lastPlayer == "black") == win]
