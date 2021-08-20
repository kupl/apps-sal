M = {}


def least_bribes(b):
    return bribes(tuple(b))


def bribes(b):
    if b not in M:
        M[b] = sum(b) if len(b) < 3 else max(b[0], b[-1]) + b[1] if len(b) == 3 else min((b[i] + max(bribes(b[:i]), bribes(b[i + 1:])) for i in range(1, len(b) - 1)))
    return M[b]
