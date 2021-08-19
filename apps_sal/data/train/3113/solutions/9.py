def distribute(m, n):
    if m < 0:
        m = 0
    if n <= 0:
        return []
    minCandiesPerPerson = m // n
    rest = m - n * minCandiesPerPerson
    return [minCandiesPerPerson] * (n - rest) + [minCandiesPerPerson + 1] * rest
