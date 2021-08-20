def pop_shift(s):
    l1 = list(s)
    l2 = []
    l3 = []
    while len(l1) > 1:
        l2.append(l1.pop())
        l3.append(l1.pop(0))
    return [''.join(l2), ''.join(l3), ''.join(l1)]
