def cnt(x):
    return sum(x[-i - 1] - x[i] for i in range(len(x) // 2))


for _ in range(int(input())):
    n, c = map(int, input().split())
    d = {}
    for i in range(n):
        x, y = map(int, input().split())
        k = (x - y, x % c)
        if k in d:
            d[k].append(x // c)
        else:
            d[k] = [x // c]
    print(len(d), sum(cnt(sorted(v)) for v in d.values()))
