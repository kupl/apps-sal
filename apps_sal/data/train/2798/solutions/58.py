def to_alternating_case(string):
    l = []
    for i in string:
        if i.upper() == i:
            l.append(i.lower())
        else:
            l.append(i.upper())
    return ''.join(l)
