def rps(p1, p2):
    r, s, p = 'rock', 'scissors', 'paper'
    if p1 == p2:
        return "Draw!"
    elif (p1,p2) in [(r,s), (s,p), (p,r)]:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

