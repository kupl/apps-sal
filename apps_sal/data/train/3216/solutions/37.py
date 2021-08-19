import math


def movie(card, ticket, perc):
    finnished = False
    n = 0
    previous_total = 0
    while not finnished:
        n += 1
        a = ticket * n
        previous_total += ticket * perc ** n
        b = math.ceil(card + previous_total)
        if a > b:
            finnished = True
    return n
