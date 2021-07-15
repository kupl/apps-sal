from math import ceil
def movie(card, ticket, perc):
    cs, ts, i = card+ticket*perc, ticket, 2
    while ceil(ts)<=ceil(cs):
        cs, ts, i = cs + ticket*perc**i, ts + ticket, i + 1
    return i-1

