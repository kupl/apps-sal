for _ in range(int(input())):
    (n, k, d) = list(map(int, input().split()))
    a = sum(map(int, input().split()[:n]))
    da = a // k
    if da >= d:
        print(d)
    else:
        print(da)
