import math


def movie(card, ticket, perc):
    (sysA, sysB, count) = (ticket, card + ticket * perc, 1)
    while sysA <= math.ceil(sysB):
        sysA += ticket
        sysB += ticket * perc ** (count + 1)
        count += 1
    return count
