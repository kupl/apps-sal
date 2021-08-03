def invert(lst):
    i = 0
    inv = []
    while i < len(lst):
        inv.append(lst[i] * -1)
        i += 1
    return inv
