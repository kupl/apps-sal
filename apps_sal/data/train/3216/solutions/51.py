import math


def movie(card, ticket, perc):
    n = 1
    ticket_b = ticket
    ticket_total = 0
    sys_a = ticket
    sys_b = card + ticket
    c = ((sys_b)) / ((sys_a))
    if (c < 1):
        return 1
        exit
    else:
        while True:
            sys_a = (n) * ticket
            ticket_b = ticket_b * perc
            ticket_total = ticket_total + ticket_b
            sys_b = card + ticket_total
            if (math.ceil(sys_b) < sys_a):
                return n
            else:
                n += 1
    return n
