T = int(input())
for i in range(T):
    (N, K) = list(map(int, input().strip().split()))
    if K != 0:
        x = N % K
        print(int(N // K), int(x))
    if K == 0:
        print(K, N)
