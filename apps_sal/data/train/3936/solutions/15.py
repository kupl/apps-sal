def zozonacci(pattern, n):
    bind = {'fib': [[0, 0, 0, 1], lambda arr: sum(arr[-2:])],
            'jac': [[0, 0, 0, 1], lambda arr: sum([2 * arr[-2], arr[-1]])],
            'pad': [[0, 1, 0, 0], lambda arr: sum([arr[-3], arr[-2]])],
            'pel': [[0, 0, 0, 1], lambda arr: sum([arr[-2], 2 * arr[-1]])],
            'tet': [[0, 0, 0, 1], lambda arr: sum(arr[-4:])],
            'tri': [[0, 0, 0, 1], lambda arr: sum(arr[-3:])]}
    if not pattern or n == 0:
        return []
    res = bind[pattern[0]][0]
    q, r = divmod(n - len(res), len(pattern))
    for v in (q * pattern + pattern[:r]):
        res.append(bind[v][1](res))
    return res[:n]
