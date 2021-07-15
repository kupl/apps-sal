def whoseMove(lastPlayer, win):
    if lastPlayer == "white":
        other_player = "black"
    else:
        other_player = "white"
    return lastPlayer if win is True else other_player
