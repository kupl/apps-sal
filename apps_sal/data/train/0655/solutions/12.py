for _ in range(int(input())):
    (N, K, V) = map(int, input().split())
    A = list(map(int, input().split()))[:N]
    S = (N + K) * V
    B = S - sum(A)
    if B > 0:
        if B % K == 0:
            print(B // K)
        else:
            print(-1)
    else:
        print(-1)
