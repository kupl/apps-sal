import math


def movie(card, ticket, perc):
    A = 0
    B = card
    i = 0

    while math.ceil(B) >= A:
        i = i + 1
        A = A + ticket
        B = B + ticket * perc**i

    return i
