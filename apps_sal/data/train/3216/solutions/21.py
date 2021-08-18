import math


def movie(card, ticket, perc):
    n = 0
    while True:
        n += 1
        A = ticket * n
        B = card + ticket * (perc * (1 - perc**n) / (1 - perc))
        if math.ceil(B) < A:
            break

    return n
