def string_constructing(a, s):
    (i, r) = (0, 1)
    for x in s:
        y = a[i % len(a)]
        while x != y:
            r += 1
            i += 1
            y = a[i % len(a)]
        i += 1
    return r + i // len(a) + -i % len(a) - (i % len(a) == 0)
