import math


def movie(card, ticket, perc):
    # we want
    # ticket*n > card + ticket*sum(p^i,where i=1 to n)
    # we use the geom series formula to simplify sum()
    n = 0
    while True:
        n += 1
        A = ticket * n
        B = card + ticket * (perc * (1 - perc**n) / (1 - perc))
        if math.ceil(B) < A:
            break

    return n
