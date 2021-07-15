def whoseMove(lastPlayer, win):
    players=['white', 'black']
    if win: return lastPlayer
    else:
      players.remove(lastPlayer)
      return players[0]
