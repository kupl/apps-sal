for t in range(int(input())):
    n, k = list(map(int, input().split()))
    poles = list(map(int, input().split()))
    dist = list(map(int, input().split()))
    d = {}
    pd = []
    for i in range(1, n):
        pd.append(poles[i] - poles[i - 1])
        d[pd[-1]] = d.get(pd[-1], 0) + 1
    m = float("inf")
    for i in dist:
        m = min(m, d[i])
    c = 0
    for i in range(n - k):
        flag = 1
        for j in range(k):
            if (pd[i + j] != dist[j]):
                flag = 0
                break
        if (flag == 1):
            c += 1
            if (c == m):
                break
    print(c)
