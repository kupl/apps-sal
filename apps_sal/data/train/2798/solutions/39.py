def to_alternating_case(s):
    return ''.join(c.upper() if c.islower() else c.lower() if c.isupper() else c for c in s)
