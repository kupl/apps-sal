d = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
def ret(fn, c1, c2, t): return f"The {['first','second'][eval(fn)]} card won." if fn else "Let us play again."


def card_game(c1, c2, t):
    return ret('d.index(c1[:-1])<d.index(c2[:-1])' if c1[-1] == c2[-1] else
               'c2=="joker"' if 'joker' in [c1, c2] else
               'c2[-1]==t' if t in [c1[-1], c2[-1]] else
               '', c1, c2, t) if c1 != c2 else "Someone cheats."  # no effeciency due to eval :(
