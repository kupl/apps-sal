from math import ceil
def movie(card, ticket, perc):
    n=1
    while True:
        card = card+ticket*perc**n
        ticket_price = ticket*n
        if ticket_price > ceil(card):
            return n
        n+=1

