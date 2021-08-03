from math import ceil


def movie(card, ticket, perc):
    N = 1
    while ticket * N <= ceil(card + ticket * perc * (1 - perc**N) / (1 - perc)):
        N += 1
    return N
