def digits(x): return set(str(x))


def LDTA(n):
    if digits(n) == digits(n * n):
        return None

    seen = []
    x = n

    while len(seen) < 10:
        for d in str(x):
            if d not in seen:
                seen.append(d)
        x *= n

    return int(seen[-1])
