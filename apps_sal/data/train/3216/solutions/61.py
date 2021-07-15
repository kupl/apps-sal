from math import *
def movie(card, ticket, perc):
    n=0
    priceA=0
    priceB=card
    while ceil(priceB)>=priceA:
        n+=1
        priceA+=ticket
        priceB+=ticket*(perc**n)
    return n
