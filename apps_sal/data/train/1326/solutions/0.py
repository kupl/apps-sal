for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    sum1 = f[0]
    d = 0
    i = 1
    while sum1 != 0 and i < n:
        sum1 = sum1 - 1 + f[i]
        d += 1
        i += 1
    print(d + sum1)
