from math import *
def movie(card, ticket, perc):
    n = 0
    seance = 0
    a = card
    ticket_abonnement = 0
    while ceil(a + ticket_abonnement) >= (ticket * seance) :
            ticket_abonnement += (ticket * perc) * perc**n
            n += 1
            seance += 1
    return seance
