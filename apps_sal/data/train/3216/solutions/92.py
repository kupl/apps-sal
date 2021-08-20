from math import ceil


def movie(card, ticket, perc):
    n = 0
    while True:
        n += 1
        sysA = ticket * n
        sysB = ceil(card + ticket * perc * (1 - perc ** n) / (1 - perc))
        if sysA > sysB:
            return n
