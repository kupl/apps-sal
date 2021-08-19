for _ in range(int(input())):
    (N, K) = map(int, input().rstrip().split())
    L1 = [i for i in range(N - K, N + 1)]
    L2 = [i for i in range(1, N - K)]
    print(*L1, *L2)
'\nN=5, K=2 => N-K+1 = 4    (1,2,3)\n      3 -> 4 -> /5/ -> 1 -> 2\n'
