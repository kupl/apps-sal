import math


def movie(card, ticket, perc):
    sys_a = 0
    sys_b = card
    i = 1
    while sys_a <= math.ceil(sys_b):
        sys_a += ticket
        sys_b += ticket * (perc**i)
        i += 1
    return i - 1
