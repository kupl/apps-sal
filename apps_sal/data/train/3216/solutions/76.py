import math 
def movie(card, ticket, perc):
    n = 0
    c = 0
    x = ticket
    while c <= math.ceil(card):
        n += 1
        c += ticket
        x *= perc
        card += x
    return n
