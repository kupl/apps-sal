def negation_value(s, val):
    if len(s) % 2:
        return not val
    else:
        return not not val
