import math
def movie(card, ticket, perc):
    a, count = ticket, 1
    ticket_p = perc*ticket
    b = card + ticket_p
    while a <= math.ceil(b):
        a += ticket
        ticket_p *= perc
        b += ticket_p
        count += 1
    return count 
