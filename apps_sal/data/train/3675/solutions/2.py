def negation_value(s, val):
    return bool(val) if len(s) % 2 == 0 else not val
