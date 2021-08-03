import math


def movie(card, ticket, perc):
    reduced = ticket * perc
    total = card + reduced
    n = 1
    while math.ceil(total) >= ticket * n:
        reduced *= perc
        total += reduced
        n += 1
    return n
