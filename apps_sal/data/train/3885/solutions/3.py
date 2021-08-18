def sumSquaresToN(n): return n * (n + 1) * (2 * n + 1) // 6


memo = set()


def values(n):
    lastMax = max(memo) if memo else 0
    if lastMax >= n:
        return sum(x < n for x in memo)

    top = int((1 + (1 + 2 * (n - 1))**.5) // 2)
    for a in range(top, 1, -1):
        va = sumSquaresToN(a)
        if va <= lastMax:
            break

        for b in range(a - 2, -1, -1):
            v = va - sumSquaresToN(b)
            if v >= n:
                break
            if v == int(str(v)[::-1]):
                memo.add(v)

    return len(memo)
