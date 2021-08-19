def rps(p1, p2):
    m = ['rock', 'paper', 'scissors']
    return ['Draw!', 'Player 1 won!', 'Player 2 won!'][m.index(p1) - m.index(p2)]
