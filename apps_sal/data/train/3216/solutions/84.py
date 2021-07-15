import math
def movie(card, ticket, perc):
    tickets = 1
    system_a = ticket
    system_b = card + (ticket * perc)
    while True:
        if math.ceil(system_b) < system_a:
            return tickets
        tickets += 1
        system_a += ticket
        system_b += ticket * perc ** tickets
