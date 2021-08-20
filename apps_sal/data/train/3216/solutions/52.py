import math


def movie(card, ticket, perc):
    i = 1

    def lhs():
        return ticket * i

    def rhs():
        return math.ceil(card + ticket * (1 - perc ** i) / (1 - perc))
    while lhs() <= rhs():
        i *= 2
    low = i / 2 - 1
    high = i + 1
    while low + 1 != high:
        i = (low + high) // 2
        if lhs() <= rhs():
            low = i
        else:
            high = i
    p_lhs = lhs()
    i += 1
    if p_lhs > rhs():
        return i - 2
    return i - 1
