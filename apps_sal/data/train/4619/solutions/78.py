def whoseMove(lastPlayer, win):
    other = ""
    if lastPlayer == "black":
        other = "white"
    else:
        other = "black"
    if win:
        return lastPlayer
    return other
