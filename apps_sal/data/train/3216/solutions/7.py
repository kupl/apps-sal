def movie(card, ticket, perc, n=1):
    while card + ticket * perc * (1 - perc ** n) / (1 - perc) - ticket * n > -1:
        n += 1
    return n
