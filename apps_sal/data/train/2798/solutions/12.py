def to_alternating_case(string):
    res = []
    for i in list(string):
        if i.isupper():
            res.append(i.lower())
        else:
            res.append(i.upper())
    return ''.join(res)
