def to_alternating_case(string):
    s = ''
    for l in string:
        if l == l.upper():
            l = l.lower()
            s += l
        else:
            l = l.upper()
            s += l
    return s
