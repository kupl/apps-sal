def whoseMove(lastPlayer, win):
    return {'white': 'black', 'black': 'white'}.get(lastPlayer) if not win else lastPlayer
