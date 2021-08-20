import math


def movie(card, ticket, perc):
    system_a: int = 0
    n: int = 0
    system_b = card
    ticket_b = ticket * perc
    while system_a <= math.ceil(system_b):
        n += 1
        system_a = ticket * n
        system_b += ticket_b
        ticket_b = ticket_b * perc
    system_b = math.ceil(system_b)
    print(f'system A price is {system_a}')
    print(f'system B price is {system_b}')
    return n
