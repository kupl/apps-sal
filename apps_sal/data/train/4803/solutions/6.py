def two_sum(n, target):
    for i in range(len(n) - 1):
        if target - n[i] in n[i + 1:]:
            return [i, n[i + 1:].index(target - n[i]) + (i + 1)]
    return None
