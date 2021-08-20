def rps(p1, p2):
    return (lambda a: 'Draw!' if a == 0 else 'Player 1 won!' if a % 3 == 2 else 'Player 2 won!')(['paper', 'rock', 'scissors'].index(p1) - ['paper', 'rock', 'scissors'].index(p2))
