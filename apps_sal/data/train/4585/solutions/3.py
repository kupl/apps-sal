def find(a, b, n):
    s = str(a) + str(b)

    while s[-3:] not in {"000", "112", "145"}:
        s += str(int(s[-2]) + int(s[-1]))

    base = len(s) - 3
    loop = {"000": "000",
            "112": "1123581347",
            "145": "1459"}[s[-3:]]

    return int(s[n]) if n < base else int(loop[(n - base) % len(loop)])
