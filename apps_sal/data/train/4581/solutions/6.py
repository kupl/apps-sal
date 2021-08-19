def are_similar(a, b):
    swap = 0
    for (idx, x) in enumerate(a):
        if a.count(x) != b.count(x):
            return False
        if x != b[idx]:
            swap += 1
            if swap > 2:
                return False
    return True
