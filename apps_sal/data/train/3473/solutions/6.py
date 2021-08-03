def doubles(s):
    for _ in range(99):
        for a, b in zip(s, s[1:]):
            if a == b:
                s = s.replace(a + b, '')
                break
    return s
