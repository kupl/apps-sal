def addsup(a1, a2, a3):
    a4 = []
    for n1 in a1:
        for n2 in a2:
            if n1 + n2 in a3:
                a4.append([n1, n2, n1 + n2])
    return a4
