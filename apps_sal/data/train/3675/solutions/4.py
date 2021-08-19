def negation_value(s, val):
    return [bool(val), not val][len(s) % 2]
