from math import ceil
def movie(card, ticket, perc):
    true = ticket
    sys_b = card
    count = 0
    while True:
        count += 1
        sys_a = count*true
        ticket = perc*ticket
        sys_b += ticket
        if ceil(sys_b)<sys_a:
            return count
    return count

