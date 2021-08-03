def monkey_count(n):
    s = []
    for i in range(n + 1):
        s += [i]
    return s[1:]
