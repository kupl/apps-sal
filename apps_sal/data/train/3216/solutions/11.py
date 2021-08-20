import math


def movie(card, ticket, perc):
    sysa = n = 0
    sysb = card
    while math.ceil(sysb) >= sysa:
        n += 1
        sysa += ticket
        sysb += ticket * math.pow(perc, n)
    else:
        return n
