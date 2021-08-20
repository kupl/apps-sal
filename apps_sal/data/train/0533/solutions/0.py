for _ in range(int(input())):
    (m, n) = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    l = -1
    for i in range(n - 1, -1, -1):
        if a[i] == m:
            l = i
            break
    f = -1
    for i in range(0, n):
        if a[i] == m:
            f = i
            break
    print(l - f)
