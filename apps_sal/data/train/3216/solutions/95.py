import math


def movie(card, ticket, perc):
    priceA = 0
    priceB = card
    visits = 0
    while priceA <= math.ceil(priceB):
        visits += 1
        priceB += ticket * perc ** visits
        priceA += ticket
    return visits
