import math


def movie(card, ticket, perc):
    n = 1
    while 1:
        if (ticket * n > card + math.ceil(ticket * (1 - pow(perc, n)) / (1 - perc))):
            return n - 1
        n = n + 1
