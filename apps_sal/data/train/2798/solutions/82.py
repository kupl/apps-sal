def to_alternating_case(string):
    s = ""
    for l in string:
        if l.lower() == l:
            s += l.upper()
        elif l.upper() == l:
            s += l.lower()
        else:
            s += l
    return s
