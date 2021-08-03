import math


def movie(card, ticket, perc):
    num_trips = 0
    card_cost = card
    ticket_cost = 0
    while math.ceil(card_cost) >= ticket_cost:
        num_trips += 1
        card_cost += ticket * (perc ** num_trips)
        ticket_cost += ticket
    return num_trips
