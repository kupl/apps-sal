def trouble(x, t):
    n = x[:1]
    for i in x[1:]:
        if i + n[-1] != t:
            n.append(i)
    return n
