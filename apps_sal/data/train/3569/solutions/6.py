def is_lucky(ticket):
    return False if len(ticket) != 6 or not ticket.isdigit() else sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))
