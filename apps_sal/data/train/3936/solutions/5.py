def zozonacci(pattern, length):
    n = len(pattern)
    if n == 0 or length == 0:
        return []
    GEN = {'fib': lambda x: x[-1] + x[-2], 'jac': lambda x: x[-1] + 2 * x[-2], 'pad': lambda x: x[-2] + x[-3], 'pel': lambda x: 2 * x[-1] + x[-2], 'tet': lambda x: x[-1] + x[-2] + x[-3] + x[-4], 'tri': lambda x: x[-1] + x[-2] + x[-3]}
    seq = [0, 1, 0, 0] if pattern[0] == 'pad' else [0, 0, 0, 1]
    for i in range(length - 4):
        seq += [GEN.get(pattern[i % n])(seq)]
    return seq[:length]
