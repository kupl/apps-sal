def string_func(s, n):
    L2 = len(s) // 2
    l = [s]
    s = list(s)
    while True:
        (s[0::2], s[1::2]) = (s[:L2 - 1:-1], s[:L2])
        l.append(''.join(s))
        if l[0] == l[-1]:
            del l[-1]
            break
    return l[n % len(l)]
