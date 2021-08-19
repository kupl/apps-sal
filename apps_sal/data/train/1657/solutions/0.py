def string_func(s, n):
    (l, s) = ([s], list(s))
    while True:
        (s[::2], s[1::2]) = (s[:len(s) // 2 - 1:-1], s[:len(s) // 2])
        l.append(''.join(s))
        if l[0] == l[-1]:
            del l[-1]
            break
    return l[n % len(l)]
