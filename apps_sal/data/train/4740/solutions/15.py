def row_sum_odd_numbers(n):
    a = [y * [False] for y in range(1, n + 1)]
    odds = iter(list(range(1, 10**6, 2)))
    return sum([[next(odds) for c in x if c is False] for x in a][-1])
