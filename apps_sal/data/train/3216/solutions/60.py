import math


def movie(card, ticket, perc):
    times = 0
    price_A = 0
    price_B = card
    while math.ceil(price_B) >= price_A:
        times += 1
        price_A += ticket
        price_B = price_B + ticket * perc ** times
    return times
