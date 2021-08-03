SEQUENCE = [2, 1]


def lucasnum(n):
    try:
        return SEQUENCE[abs(n)] * (1, -1)[n < 0 and n % 2]
    except IndexError:
        while len(SEQUENCE) < abs(n) + 1:
            SEQUENCE.append(SEQUENCE[-1] + SEQUENCE[-2])
        return lucasnum(n)
