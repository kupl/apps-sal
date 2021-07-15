def solve(l):
    l1 = []
    for i, _ in enumerate(l):
        l1.append(list([ord(x.lower()), i+97] for i, x in enumerate(l[i])
                        if ord(x.lower()) == i+97))
        l2 = [len(x) for x in l1]
    return l2
