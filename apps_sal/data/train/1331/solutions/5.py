T = int(input())
for _ in range(T):
    X, K = [int(x) for x in input().split()]

    k, x, y = 1, 2, 1
    while x <= K:
        k, x, y = k + 1, x * 2, x

    print((X / x) + (K - y) * X / y)
