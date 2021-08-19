for _ in range(int(input())):
    (m, n) = list(map(int, input().split()))
    l = len(str(n))
    last = m
    for i in range(1, 12):
        if 10 ** i - 1 > n:
            break
    if i == 1:
        print(0, 0)
    else:
        print(m * (i - 1), m)
