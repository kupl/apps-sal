def rps(p1, p2):
    return "Draw!" if p1 == p2 else "Player {} won!".format(-~(p2[0] + p1[0] in "rspr"))
