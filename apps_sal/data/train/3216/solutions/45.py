from math import ceil
def movie(card, ticket, perc):
    priceA=ticket
    priceB=card+ticket*perc
    n=1
    while ceil(priceB) >= priceA:
        n+=1
        priceA+=ticket
        priceB+=ticket*perc**n
    return n        
