def rps(p1, p2):
    p1c = ['p1rp2s', 'p1sp2p', 'p1pp2r']
    p2c = ['p1sp2r', 'p1pp2s', 'p1rp2p']
    p1w = "Player 1 won!"
    p2w = "Player 2 won!"
    p3w = "Draw!"
    i = "p1{}p2{}".format(p1[0], p2[0])
    return p1w if i in p1c else p2w if i in p2c else p3w
