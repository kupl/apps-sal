def survivor(n):
    idx, i = n, 2
    while idx % i != 0 and idx > i:
        idx -= idx // i
        i += 1
    return idx % i != 0
