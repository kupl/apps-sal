import math
def movie(card, ticket, perc):
    n = 0
    A = 0.0
    B = card
    while math.ceil(B) >= A:
        n += 1
        A += ticket
        B += ticket * (perc ** n)
    return n
