from math import ceil

def movie(card, ticket, perc):
    n = 1
    p = card + ticket*perc
    while ceil(p)>=n*ticket:
        n += 1
        p += ticket*(pow(perc,n))
    return n
