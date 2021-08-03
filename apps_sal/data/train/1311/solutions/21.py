for _ in range(int(input())):
    N, K = map(int, input().split())
    cumsum = 0
    coupo = 0
    coune = 0
    for i in range(N):
        if coupo == K:
            print(-(i + 1), end=' ')
            coune += 1
            continue
        elif coune == N - K:
            print((i + 1), end=' ')
            coupo += 1
            continue
        a = cumsum + (i + 1)
        b = cumsum - (i + 1)
        if abs(a) > abs(b):
            cumsum = b
            print(-(i + 1), end=' ')
        else:
            cumsum = a
            print((i + 1), end=' ')
        if cumsum > 0:
            coupo += 1
        else:
            coune += 1
