import math


def movie(card, ticket, perc):
    total = card
    n = 1
    while True:
        total += ticket * perc ** n
        if math.ceil(total) < ticket * n:
            break
        n += 1
    return n
