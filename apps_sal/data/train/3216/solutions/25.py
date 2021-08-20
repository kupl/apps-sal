import math


def movie(card, ticket, perc):
    x = 1
    systema = 0
    systemb = card
    while systemb >= systema:
        systema = ticket * x
        systemb += ticket * perc ** x
        if math.ceil(systemb) < systema:
            break
        else:
            x += 1
    return x
