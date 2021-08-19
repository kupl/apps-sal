from math import ceil


def movie(card, ticket, perc):
    # your code
    discount_ticket = ticket
    system_a_price = 0
    system_b_price = card
    days = 0
    while ceil(system_b_price) >= system_a_price:
        days = days + 1
        discount_ticket = discount_ticket * perc
        system_a_price = days * ticket
        system_b_price = system_b_price + discount_ticket
    return days
