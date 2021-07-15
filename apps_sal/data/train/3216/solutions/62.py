import math

def movie(card, ticket, perc):
    sys_a = 0
    sys_b = card
    time = 0
    while sys_a <= math.ceil(sys_b):
        time += 1
        sys_a = ticket * time
        sys_b += ticket * (perc ** time)
    return time
