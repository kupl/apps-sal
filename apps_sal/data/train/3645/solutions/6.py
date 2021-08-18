def diff(a, b):
    c = []
    for i in a:
        if i not in b and i not in c:
            c.append(i)
    for i in b:
        if i not in a and i not in c:
            c.append(i)

    return sorted(c)
