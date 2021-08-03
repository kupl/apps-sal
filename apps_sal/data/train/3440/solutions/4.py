pows = [2**i for i in range(63, -1, -1)]


def powers(n):
    result = []
    for p in pows:
        if n >= p:
            result.append(p)
            n -= p
    return result[::-1]
