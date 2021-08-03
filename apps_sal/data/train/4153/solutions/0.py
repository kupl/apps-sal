S, SS, SUM = [0], {0}, [0]


def rec(n):
    while len(S) <= n:
        v = S[-1] - len(S)
        if v <= 0 or v in SS:
            v += 2 * len(S)
        S.append(v)
        SS.add(v)
        SUM.append(SUM[-1] + v)
    return SUM[n - 1]
