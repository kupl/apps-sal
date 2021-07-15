from math import ceil
def movie(card, ticket, perc):
    n = 0;
    while 1:
        n+= 1
        if ticket*n>ceil(card+ticket*perc*(1-perc**n)/(1-perc)):
            return n
