import math

def movie(card, ticket, perc):
    PriceA = 0
    PriceB = card
    n = 0
    while PriceA <= math.ceil(PriceB):
        n += 1
        PriceA += ticket
        PriceB += ticket * (perc ** n)
    return n
