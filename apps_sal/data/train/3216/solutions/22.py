import math


def movie(card, ticket, perc):
    a, b, n = 0, card, 0
    while math.ceil(b) >= a:
        n += 1
        a += ticket
        b += ticket * (perc ** n)
    return n
