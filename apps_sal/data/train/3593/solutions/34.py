def capitalize(s, ind):
    t = ''
    for (num, x) in enumerate(s):
        if num in ind:
            t += x.upper()
        else:
            t += x
    return t
