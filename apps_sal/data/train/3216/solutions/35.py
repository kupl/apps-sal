import math


def movie(card, ticket, perc):
    Aval, Bval, res = ticket, card + (ticket * perc), 1
    while math.ceil(Bval) >= Aval:
        res += 1
        Aval += ticket
        Bval += ticket * (perc**res)
    return res
