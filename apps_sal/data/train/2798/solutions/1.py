def to_alternating_case(string):
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])
