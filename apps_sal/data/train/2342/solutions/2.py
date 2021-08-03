t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n - 1)
    for i in range(n - 1):
        b[i] = a[i + 1] - a[i]
    mi = 10000000
    c = [0] * (n + 1)
    for i in range(n - 1):
        if b[i] < 0:
            c[i + 1] += b[i]
            c[0] -= b[i]
        else:
            c[i + 1] += b[i]
            c[-1] -= b[i]
    for i in range(n):
        c[i + 1] += c[i]
    for i in range(n):
        if c[i] > a[i]:
            print('NO')
            break
    else:
        print('YES')
