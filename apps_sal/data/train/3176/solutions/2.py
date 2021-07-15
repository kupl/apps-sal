def to_cents(amount):
    if amount and amount[0] == '$':
        try:
            return int(amount[1:-3] + amount[-2:])
        except:
            return None
    return None
