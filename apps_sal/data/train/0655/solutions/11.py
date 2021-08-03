for _ in range(int(input())):
    N, K, v = list(map(int, input().split()))
    a = list(map(int, input().split()))[:N]
    s = (N + K) * v
    b = s - sum(a)
    if b > 0:
        if b % K == 0:
            print(b // K)
        else:
            print(-1)
    else:
        print(-1)
