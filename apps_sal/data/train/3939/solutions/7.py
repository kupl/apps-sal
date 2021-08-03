def rps(a, b): return ['Draw!', 'Player 1 won!', 'Player 2 won!'][('srp'.index(a[0]) - 'srp'.index(b[0])) % 3]
