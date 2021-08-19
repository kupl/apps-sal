from math import *


def movie(card, ticket, perc):
    n = 1
    while ceil(card + ticket * perc * (1 - perc ** n) / (1 - perc)) >= ticket * n:
        n += 1
    return n
