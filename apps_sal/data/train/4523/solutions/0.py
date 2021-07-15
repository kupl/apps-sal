def solve(n):
    x = str(n)
    res = [x] + [str(int(x[:i]) - 1) + '9' * (len(x) - i) for i in range(1, len(x))]
    return int(max(res, key=lambda x: (sum(map(int, x)), int(x))))
