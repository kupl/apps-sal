players = ['white', 'black']
def whoseMove(lastPlayer, win):
    return players[(players.index(lastPlayer) + (not win)) % len(players)]
