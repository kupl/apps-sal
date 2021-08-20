import math


def movie(card, ticket, perc):
    tiks = 0
    sysA = 0
    sysB = card
    Bticket = ticket
    while math.ceil(sysB) >= sysA:
        sysA += ticket
        tiks += 1
        Bticket *= perc
        sysB += Bticket
    return tiks
