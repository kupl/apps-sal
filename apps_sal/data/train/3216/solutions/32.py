from math import ceil


def movie(card, ticket, perc):
    (a, b, c) = (0, card, 0)
    while ceil(b) >= ceil(a):
        a += ticket
        b += ticket * perc ** c
        c += 1
    return c - 1
