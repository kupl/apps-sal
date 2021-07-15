def is_lucky(ticket):
    try:
        y = int(ticket)
    except ValueError:
        return False
    return sum([int(x) for x in ticket[0:3]]) == sum([int(x) for x in ticket[3:]]) 
