from math import ceil

def movie(card, ticket, perc):
    num = 0
    priceA = 0
    priceB = card
    while ceil(priceB) >= priceA:
        num += 1
        priceA += ticket
        priceB += ticket * (perc ** num)
    return num
