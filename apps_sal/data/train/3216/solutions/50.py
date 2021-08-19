def movie(card, ticket, perc):
    import math
    n = 1
    s1 = ticket
    s2 = card + ticket * perc
    while s1 <= math.ceil(s2):
        n += 1
        s1 = ticket * n
        s2 += ticket * perc ** n
    return n
