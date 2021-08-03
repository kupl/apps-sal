def sumSquaresToN(n): return n * (n + 1) * (2 * n + 1) // 6


memo = set()


def values(n):
    lastMax = max(memo) if memo else 0
    if lastMax >= n:
        return sum(x < n for x in memo)

    top = int((1 + (1 + 2 * (n - 1))**.5) // 2)           # Value of the top number for a sum of two consecutive squares under n: (top-1)**2 + top**2 <= n
    for a in range(top, 1, -1):
        va = sumSquaresToN(a)                         # sum of squares of 1, 2, 3, ..., a
        if va <= lastMax:
            break                       # va is greater than all the values generated with the inner loop, so if too small to generate new values, exit

        for b in range(a - 2, -1, -1):
            v = va - sumSquaresToN(b)                 # current value
            if v >= n:
                break                          # going down with the values of b, v increase at each execution. Allow to exit the loop when generated values become to big (and useless for the current call)
            if v == int(str(v)[::-1]):
                memo.add(v)

    return len(memo)
