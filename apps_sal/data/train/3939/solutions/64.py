def rps(p1, p2):
    game = ['rock', 'paper', 'scissors']
    (s1, s2) = (game.index(p1), game.index(p2))
    if s1 == s2:
        return 'Draw!'
    if s1 == 0 and s2 == 2 or (s1 == 2 and s2 == 1) or (s1 == 1 and s2 == 0):
        return 'Player 1 won!'
    return 'Player 2 won!'
