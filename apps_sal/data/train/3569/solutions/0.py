def is_lucky(ticket):
    if len(ticket) == 6 and ticket.isdigit():
        t = list(map(int, ticket))
        return sum(t[:3]) == sum(t[3:])
    return False
