from math import ceil


def movie(card, ticket, perc):
    i = 0
    sb = card
    sa = 0
    prev = ticket
    while True:
        i += 1
        nou = prev * perc
        sb += nou
        prev = nou
        sa += ticket
        if (ceil(sb) < sa):
            return i
