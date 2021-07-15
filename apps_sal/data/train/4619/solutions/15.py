def whoseMove(lastPlayer, win):
    return {'black':'white','white':'black'}.get(lastPlayer) if not win else lastPlayer
