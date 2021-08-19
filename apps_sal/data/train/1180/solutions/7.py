def res(x, y, n, k):
    d = abs(x - y)
    if x == y:
        print(n, n)
    elif x > y:
        p = k % 4
        if p == 0:
            print(d, 0)
        elif p == 1:
            print(n, n - d)
        elif p == 2:
            print(n - d, n)
        else:
            print(0, d)
    elif x < y:
        p = k % 4
        if p == 0:
            print(0, d)
        elif p == 1:
            print(n - d, n)
        elif p == 2:
            print(n, n - d)
        else:
            print(d, 0)


n = int(input())
for i in range(n):
    (n, k, x, y) = list(map(int, input().split()))
    res(x, y, n, k)
