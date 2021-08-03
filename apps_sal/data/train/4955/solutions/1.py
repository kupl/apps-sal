def ride(group, comet):
    n1 = 1
    n2 = 1
    for x in group:
        n1 *= ord(x.lower()) - 96
    for x in comet:
        n2 *= ord(x.lower()) - 96
    if n1 % 47 == n2 % 47:
        return "GO"
    else:
        return "STAY"
