def string_constructing(a, s):
    i = 0
    for c in s:
        while a[i % len(a)] != c:
            i += 1
        i += 1
    return (i + len(a) - 1) // len(a) * (len(a) + 1) - len(s)
