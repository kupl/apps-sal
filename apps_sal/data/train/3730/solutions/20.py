def capitalize(s):
    a1 = ''
    a2 = ''
    for (i, v) in enumerate(s, 1):
        if i % 2:
            a1 += v.upper()
            a2 += v.lower()
        else:
            a1 += v.lower()
            a2 += v.upper()
    return [a1, a2]
