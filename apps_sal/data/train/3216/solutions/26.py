from math import ceil


def movie(card, ticket, perc):
    prevPrice = ticket
    i = 0

    while True:
        if ceil(card) < ticket * i:
            return i
        prevPrice *= perc
        card += prevPrice
        i += 1
