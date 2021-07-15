def whoseMove(lastPlayer, win):
    players = ['white', 'black']
    return lastPlayer if win else players[players.index(lastPlayer) - 1]
