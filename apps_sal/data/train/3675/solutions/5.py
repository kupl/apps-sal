def negation_value(s, val):
    if len(s) % 2 == 0:
        return bool(val)
    else:
        return not bool(val)

