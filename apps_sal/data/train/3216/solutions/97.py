import math


def movie(card, ticket, perc):
    count = 0
    system_A = 0
    system_B = card
    while math.ceil(system_B) >= system_A:
        count += 1
        system_A += ticket
        system_B += ticket * perc ** count
    return count
