def rps(p1, p2):
    sc = 'scissors'
    pp = 'paper'
    rc = 'rock'
    inpt = [p1, p2]
    if inpt == [sc, pp] or inpt == [rc, sc] or inpt == [pp, rc]:
        return 'Player 1 won!'
    if inpt == [pp, sc] or inpt == [sc, rc] or inpt == [rc, pp]:
        return 'Player 2 won!'
    else:
        return 'Draw!'
