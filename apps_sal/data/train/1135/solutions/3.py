t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = []
    c = n
    for i in range(n):
        a.append(c)
        c = c - 1
    a[0:k + 1] = reversed(a[0:k + 1])
    print(*a)
