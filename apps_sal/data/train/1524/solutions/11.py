def __starting_point():
    T = int(input())
    for i in range(T):
        (N, K) = list(map(int, input().split()))
        val = K * pow(K - 1, N - 1)
        print(val % 1000000007)


__starting_point()
