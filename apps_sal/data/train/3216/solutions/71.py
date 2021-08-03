from math import ceil


def movie(card, ticket, perc):
    sysa = 0
    sysb = card
    ratio = ticket * perc
    times = 0

    while sysa <= ceil(sysb):
        sysa += ticket
        sysb += ratio
        ratio *= perc
        times += 1

    return times
