def is_lucky(ticket):
    return True if len(ticket) == 6 and ticket.isnumeric() and sum([int(i) for i in ticket[:3]]) == sum([int(i) for i in ticket[3:]]) else False
