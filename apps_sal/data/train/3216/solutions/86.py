import math
def movie(card, ticket, perc):
    tickets = 1
    ticket_a = ticket
    ticket_b = card+ticket*perc
    while True:
        if math.ceil(ticket_b) < ticket_a:
            return tickets
        ticket_a += ticket
        ticket_b += ticket*(perc**(tickets+1))
        tickets += 1
