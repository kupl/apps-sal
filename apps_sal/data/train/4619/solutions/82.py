def whoseMove(lastPlayer, win):
    loser = {"white": "black", "black": "white"}
    winer = {"black": "black", "white": "white"}

    if win:
        return winer[lastPlayer]
    else:
        return loser[lastPlayer]
