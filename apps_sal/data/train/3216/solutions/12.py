import math


def movie(card, ticket, perc):
    n = 0
    a_price = 0
    b_price = card
    perc_multiplier = perc
    while math.ceil(b_price) >= a_price:
        a_price += ticket
        b_price += ticket * perc_multiplier
        perc_multiplier *= perc
        n += 1
    return n
