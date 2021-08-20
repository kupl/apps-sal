def rps(p1, p2):
    return {'rockscissors': 'Player 1 won!', 'scissorspaper': 'Player 1 won!', 'paperrock': 'Player 1 won!', 'scissorsrock': 'Player 2 won!', 'paperscissors': 'Player 2 won!', 'rockpaper': 'Player 2 won!', 'rockrock': 'Draw!', 'scissorsscissors': 'Draw!', 'paperpaper': 'Draw!'}.get(p1 + p2)
