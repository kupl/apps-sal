def negation_value(s, val):
    if val:
        a = True
    else:
        a = False
    return [a, 1 - a][s.count('!')%2]
