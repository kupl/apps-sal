from collections import defaultdict


def dec(n):
    decomp = defaultdict(lambda: 0)
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            decomp[i] += 1
        i += 1
    return decomp


def decomp(n):
    ans = defaultdict(lambda: 0)
    for i in range(2, n + 1):
        for (key, value) in dec(i).items():
            ans[key] += value
    return ' * '.join(('{}^{}'.format(x, y) if y > 1 else str(x) for (x, y) in sorted(ans.items())))
