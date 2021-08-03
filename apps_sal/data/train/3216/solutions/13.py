import math


def movie(card, ticket, perc):
    pc = card
    pt = 0
    count = 0
    while not math.ceil(pc) < math.ceil(pt):
        count += 1
        pc += ticket * (perc**count)
        pt += ticket
    return count
