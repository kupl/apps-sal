t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    l = []
    for i in range(1, n + 1):
        l.append(i)
    l.sort()
    (l[k], l[-1]) = (l[-1], l[k])
    print(*l)
