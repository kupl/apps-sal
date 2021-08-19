T = int(input().strip())
for tc in range(T):
    (N, K) = map(int, input().strip().split())
    if K == 0:
        print(0, N)
    else:
        print(N // K, N % K)
