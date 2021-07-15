def is_lucky(ticket):
    if len(ticket) == 6 and ticket.isdigit():
        return sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))
    return False
