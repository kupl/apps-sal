def whoseMove(last_player, win):
    return last_player if win else {'white': 'black'}.get(last_player, 'white')
