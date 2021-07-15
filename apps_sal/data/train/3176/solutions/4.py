from re import match

def to_cents(amount):
    res = match('^\$(\d*)\.(\d{2})(?!\n)$', amount)
    return int(''.join(res.groups())) if res else None
