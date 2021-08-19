T = int(input())
for i in range(T):
    (N, K) = map(int, input().split())
    if K != 0:
        studCandle = N % K
        print(N // K, studCandle)
    if K == 0:
        print(K, N)
