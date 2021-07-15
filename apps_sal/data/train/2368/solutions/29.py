for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = min(a)
    for i in range(len(a)):
        a[i] -= m
    m = min(b)
    for i in range(len(b)):
        b[i] -= m
    o = 0
    for i in range(n):
        o += max(a[i], b[i])
    print(o)
