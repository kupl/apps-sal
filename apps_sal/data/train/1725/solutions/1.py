def circular_limited_sums(max_n, max_fn):
    if max_n == 1:
        return sum([1 for i in range(max_fn + 1) if i + i <= max_fn]) % 12345787
    nexts = [list(filter(lambda x: i + x <= max_fn, range(max_fn + 1))) for i in range(max_fn + 1)]
    result = 0
    for ii in range(max_fn + 1):
        v = [[1 if e in nexts[ii] else 0 for e in range(max_fn + 1)]]
        for _ in range(max_n - 2):
            v.append([0 for i in range(max_fn + 1)])
            for (i, e) in enumerate(v[-2]):
                for j in nexts[i]:
                    v[-1][j] += e
        result += sum([e for (i, e) in enumerate(v[-1]) if i + ii <= max_fn])
    return result % 12345787
