def __starting_point():
    # Read number of cases
    T = int(input())
    # Run a loop for all test cases
    for i in range(T):
        # Read values
        N, K = list(map(int, input().split()))

        val = K * pow(K - 1, N - 1)
        print(val % 1000000007)


__starting_point()
