from itertools import accumulate, repeat
def squares(x, n):
    return list(accumulate(repeat(x, n), lambda a, _: a * a))
