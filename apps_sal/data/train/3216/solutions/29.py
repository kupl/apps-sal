def movie(card, ticket, perc):
    import math
    count = 1
    priceA = card
    priceB = 0
    while True:
        priceB += ticket
        priceDecrease = ticket * pow(perc, count)
        priceA += priceDecrease
        if priceB > math.ceil(priceA):
            return count
        count += 1
