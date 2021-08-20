import math


def movie(card, ticket, perc):
    x = 0
    price1 = 0
    price2 = card
    while math.ceil(price2) >= price1:
        x += 1
        price1 += ticket
        price2 += ticket * perc ** x
    return x
