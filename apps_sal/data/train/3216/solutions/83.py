import math
def movie(card, ticket, perc):
    a = 0
    b = card
    n = 0
    while math.ceil(b) >= a:
        n += 1
        a += ticket
        b += ticket * (perc ** n)
    return n
