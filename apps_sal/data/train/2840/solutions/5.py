def withdraw(n, bills=[100, 50, 20]):
    changes = [[0] * len(bills) for _ in range(n + 1)]
    for c in range(1, n + 1):
        changes[c] = min(([v + (b == bills[i]) for (i, v) in enumerate(changes[c - b])] for b in bills if c >= b), key=sum, default=[float('inf')] * len(bills))
    return changes[-1]
