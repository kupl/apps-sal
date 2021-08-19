def movie(card, ticket, perc):
    import math
    sysa = 0
    sysb = card
    tickets = 0
    while True:
        tickets += 1
        sysa += ticket
        sysb += ticket * perc ** tickets
        if math.ceil(sysb) < sysa:
            return tickets
