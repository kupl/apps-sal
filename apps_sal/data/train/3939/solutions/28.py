def rps(p1, p2):
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    p1w = 'Player 1 won!'
    p2w = 'Player 2 won!'
    if p1 == r and p2 == s: return p1w
    if p1 == r and p2 == p: return p2w
    if p1 == p and p2 == s: return p2w
    if p1 == p and p2 == r: return p1w
    if p1 == s and p2 == r: return p2w
    if p1 == s and p2 == p: return p1w
    else: return 'Draw!'

