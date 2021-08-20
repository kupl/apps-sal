for _ in range(int(input())):
    (n, k, x) = map(int, input().split())
    a = n * [0]
    for i in range(0, n, k):
        a[i] = x
    print(*a)
