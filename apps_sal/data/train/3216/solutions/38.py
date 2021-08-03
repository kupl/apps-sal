from math import ceil


def movie(card, ticket, perc):
    n = 0
    total = card
    while (ceil(total) >= n * ticket):
        total += ticket * perc**n
        n += 1

    return n - 1
