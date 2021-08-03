from math import ceil


def movie(card, ticket, perc):
    i = 1
    card = card + ticket * perc
    while True:
        if ceil(card) < i * ticket:
            return i
        else:
            i += 1
            card += ticket * (perc**i)
