def solve(n):
    res = []
    x = list(range(2, n + 1))
    while True:
        res.append(x.pop(0))
        if res[-1] > len(x):
            break
        for i in range(res[-1] - 1, len(x), res[-1]):
            x[i] = 0
        x = [i for i in x if i]
        if len(x) == 0:
            break
    return 1 + sum(res) + sum(x)
