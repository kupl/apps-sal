SEQUENCES = {'fib': (lambda s, n: s[n - 1] + s[n - 2], (0, 0, 0, 1)), 'jac': (lambda s, n: s[n - 1] + 2 * s[n - 2], (0, 0, 0, 1)), 'pad': (lambda s, n: s[n - 2] + s[n - 3], (0, 1, 0, 0)), 'pel': (lambda s, n: 2 * s[n - 1] + s[n - 2], (0, 0, 0, 1)), 'tri': (lambda s, n: s[n - 1] + s[n - 2] + s[n - 3], (0, 0, 0, 1)), 'tet': (lambda s, n: s[n - 1] + s[n - 2] + s[n - 3] + s[n - 4], (0, 0, 0, 1))}


def zozonacci(pattern, length):
    if not pattern:
        return []
    seq = list(SEQUENCES[pattern[0]][1])
    i = 0
    while len(seq) < length:
        (fn, _) = SEQUENCES[pattern[i]]
        seq.append(fn(seq, len(seq)))
        i = (i + 1) % len(pattern)
    return seq[:length]
