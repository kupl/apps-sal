def rps(p1, p2):
    r = 'rock'
    s = 'scissors'
    p = 'paper'
    if p1 == p and p2 == r or (p1 == r and p2 == s) or (p1 == s and p2 == p):
        return 'Player 1 won!'
    elif p1 == p2:
        return 'Draw!'
    else:
        return 'Player 2 won!'
