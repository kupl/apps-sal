import math


def system_a(ticket, times):
    price_a = ticket * times
    return price_a


def system_b(card, ticket, perc, times):
    price_b = 0
    it = perc * ticket
    for i in range(0, times):
        price_b = price_b + it
        it = it * perc
    price_b = price_b + card
    return price_b


def movie(card, ticket, perc):
    times = 1
    systemb = card + ticket * perc
    while math.ceil(systemb) >= system_a(ticket, times):
        systemb = systemb + perc ** (times + 1) * ticket
        times = times + 1
    return times
