import math


def movie(card, ticket, perc):
    v = 0
    i = 0
    while 1:
        i = i + 1
        if i == 1:
            v = ticket * perc
        elif i > 1:
            v = v * perc
        card += v
        if math.ceil(card) < ticket * i:
            return i
