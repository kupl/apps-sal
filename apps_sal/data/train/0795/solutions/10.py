for _ in range(int(input())):
    N, K, L = input().split(" ")
    N, K, L = int(N), int(K), int(L)
    if K * L < N or (K == 1 and N > 1):
        print(-1)
    else:
        print(*[int(i % K) + 1 for i in range(N)])
