def is_centered(a, n):
    if not n and (not len(a) % 2):
        return 1
    for i in range(sum(divmod(len(a), 2)) - 1, -1, -1):
        if sum(a[i:len(a) - i]) == n:
            return 1
    return 0
