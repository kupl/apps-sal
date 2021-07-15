for i in range(int(input())):
    t = list(map(int, input().split()))
    d = 212 * sum(q ** 2 for q in t) > sum(t) ** 2
    print(['poisson', 'uniform'][d])
