def whoseMove(lastPlayer, win):
    if win:
        return lastPlayer
    else:
        return ('black', 'white')[lastPlayer == 'black']
