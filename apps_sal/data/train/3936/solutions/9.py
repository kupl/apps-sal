def zozonacci(pat, n):
    if not pat or not n:
        return []
    d = {'fib': lambda x: sum(x[-2:]), 'jac': lambda x: x[-1] + 2 * x[-2], 'pad': lambda x: x[-2] + x[-3], 'pel': lambda x: 2 * x[-1] + x[-2], 'tet': lambda x: sum(x[-4:]), 'tri': lambda x: sum(x[-3:])}
    if pat[0] == 'pad':
        a = [0, 1, 0, 0]
    else:
        a = [0, 0, 0, 1]
    for i in range(n - 4):
        a.append(d.get(pat[i % len(pat)])(a))
    return a[:n]
