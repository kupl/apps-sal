def movie(card, ticket, perc):
    import math
    n = 1
    while n * ticket - card <= math.ceil(ticket * (perc ** n - 1) / (perc - 1)):
        n += 1
    return n - 1
