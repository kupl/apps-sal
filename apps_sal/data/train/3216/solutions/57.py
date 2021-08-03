def movie(card, ticket, perc):
    from math import ceil

    b = card
    n = 1
    while True:
        a = ticket * n
        b = b + ticket * perc**n
        if b + 1 < a:
            return n
        else:
            n = n + 1
