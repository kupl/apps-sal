def rps(p1, p2):
    a = ['paper', 'rock', 'scissors']
    if p1 == p2:
        return 'Draw!'
    return 'Player 1 won!' if p1 == a[0] and p2 == a[1] or (p1 == a[1] and p2 == a[2]) or (p1 == a[2] and p2 == a[0]) else 'Player 2 won!'
