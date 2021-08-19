for i in range(int(input())):
    (n, k, x) = map(int, input().split())
    a = []
    for i in range(n):
        if (i + 1) % k != 0:
            a.append(0)
        else:
            a.append(x)
    print(*a)
