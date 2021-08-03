

for i in range(int(input())):
    n, k = list(map(int, input().split()))

    t = []

    for j in range(n, n - k - 1, -1):
        t.append(j)
    t = t[::-1]

    p = []
    for i in range(1, n - k):
        p.append(i)

    print(*(t[:2] + p + t[2:]))
