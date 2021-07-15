def whoseMove(lastPlayer, win):
    players = ['black', 'white']
    return lastPlayer if win else players[(players.index(lastPlayer) + 1) % 2]
