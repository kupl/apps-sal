for t in range(int(input())):
    (n, m) = list(map(int, input().split()))
    x = []
    for i in range(n):
        x.append(10)
    for i in range(m):
        (i, j, k) = list(map(int, input().split()))
        for j in range(i - 1, j):
            x[j] *= k
    s = 0
    for i in range(n):
        s += x[i]
    print(int(s / n))
