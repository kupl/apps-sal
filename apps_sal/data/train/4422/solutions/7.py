def jumbled_string(s, n):
    idx = list(range(0, len(s), 2)) + list(range(1, len(s), 2))
    lst = []
    while not lst or s != lst[0]:
        lst.append(s)
        s = ''.join((s[i] for i in idx))
        if len(lst) == n:
            return s
    return lst[n % len(lst)]
