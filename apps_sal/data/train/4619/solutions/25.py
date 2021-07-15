def whoseMove(lastPlayer, win):
    players = 'blackwhite'
    if win:
        result = lastPlayer
    else:
        result = players.replace(lastPlayer, '')
    return result
