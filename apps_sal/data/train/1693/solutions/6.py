for i in range(int(input())):
    t = list(map(int, input().split()))
    p = sum(t) / 250
    d = sum((q - p) ** 2 for q in t) / 250
    print(['poisson', 'uniform'][6 * d > p * p])
