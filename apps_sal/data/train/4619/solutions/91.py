opponents = {'black': 'white', 'white': 'black'}

def whoseMove(last_player, win):
    return last_player if win else opponents[last_player]
