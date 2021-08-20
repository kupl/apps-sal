t = int(input())
for i in range(t):
    N = int(input())
    if N == 1:
        print(0)
    else:
        k = 0
        for i in range(N):
            (s, p, v) = list(map(int, input().split()))
            h = p // (s + 1) * v
            if h > k:
                k = h
        print(int(k))
