def remove_smallest(n):
    if len(n) == 0:
        return []
    c = n.count(min(n))
    print(n.index(min(n)))
    idx = n.index(min(n))
    print(c)
    a = []
    if c == 1:
        for x in n:
            if x > min(n):
                a.append(x)
    elif c > 1:
        for i in range(len(n)):
            if i != idx:
                a.append(n[i])
    return a
