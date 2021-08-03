SEEN = {0}
REC = [0]
SUM = [0, 0]


def rec(n):

    for i in range(len(REC), n + 1):
        k = REC[-1] - i
        if not (k >= 0 and k not in SEEN):
            k += i + i
        SEEN.add(k)
        REC.append(k)
        SUM.append(SUM[-1] + k)

    return SUM[n]
