for i in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    if a[0] - 1 > k:
        c += (a[0] - 1) // k
    for i in range(n - 1):
        if a[i + 1] - a[i] > k:
            c += (a[i + 1] - a[i] - 1) // k
    print(c)
