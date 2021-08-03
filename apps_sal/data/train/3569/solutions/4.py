import re


def is_lucky(ticket):
    return bool(re.match(r'\d{6}', ticket)) and sum(int(i) for i in ticket[:3]) == sum(int(i) for i in ticket[3:])
