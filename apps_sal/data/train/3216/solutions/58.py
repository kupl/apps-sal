import math


def movie(card, ticket, perc):
    sys_A, sys_B, count = ticket, card + ticket * perc, 1
    while sys_A <= math.ceil(sys_B):
        sys_A += ticket
        sys_B += ticket * (perc**(count + 1))
        count += 1
    return count
