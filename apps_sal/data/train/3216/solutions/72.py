import math


def movie(card, ticket, perc):
    a, tc = 0, 0
    tc2 = ticket
    while math.ceil(card) >= tc:
        a += 1
        ticket = ticket * perc
        tc += tc2
        card += ticket
    return a
