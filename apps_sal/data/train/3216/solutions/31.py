from math import ceil


def movie(card, ticket, perc):
    n = 0
    ap = 0
    bp = card
    price = ticket
    while ap <= ceil(bp):
        n += 1
        ap += ticket
        price = price * perc
        bp += price
    return n
