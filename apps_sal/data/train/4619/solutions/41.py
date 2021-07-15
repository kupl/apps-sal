def whoseMove(lastPlayer, win):
    return "black" if lastPlayer == "white" and not win else 'white' if lastPlayer == "black" and not win else lastPlayer

