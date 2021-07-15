import copy


def lamps(a):
    k = 0
    n = []
    b = copy.deepcopy(a)
    print(a)
    for c in range(1, len(a)):
        if a[c] == a[c - 1]:
            a[c] = 1 - a[c]
            k += 1
    if k == 0:
        return 0
    n.append(k)
    print(n)
    k = 1
    b[0] = 1 - b[0]
    print(b)
    for c in range(1, len(b)):
        if b[c] == b[c - 1]:
            b[c] = 1 - b[c]
            k += 1
    n.append(k)
    print(n)
    return min(n)

