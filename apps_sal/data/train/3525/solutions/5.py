from itertools import groupby


def flipping_game(lst):
    split = [(k, sum(1 for _ in g)) for k, g in groupby(lst)]
    zeroes = [i for i, t in enumerate(split) if not t[0]]
    return max((sum((k ^ 1 if a <= i <= b else k) * n for i, (k, n) in enumerate(split))
                for z, a in enumerate(zeroes)
                for b in zeroes[z:]),
               default=sum(lst) - 1)
