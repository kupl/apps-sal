def whoseMove(lastPlayer, win):
    players = ('black', 'white', 'black')
    return players[players.index(lastPlayer) + (not win)]
