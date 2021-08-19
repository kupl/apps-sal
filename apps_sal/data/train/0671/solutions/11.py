for _ in range(int(input())):
    (n, s) = map(int, input().split())
    P = list(map(int, input().split()))
    df = list(map(int, input().split()))
    (d, f) = (100, 100)
    for i in range(n):
        if df[i] == 0:
            if P[i] < d:
                d = P[i]
        elif P[i] < f:
            f = P[i]
    if s + d + f <= 100:
        print('yes')
    else:
        print('no')
