def whoseMove(lastPlayer, win):
    if win == True:
        return lastPlayer
    
    if lastPlayer == "white":
        return "black"
    
    else:
        return "white"
