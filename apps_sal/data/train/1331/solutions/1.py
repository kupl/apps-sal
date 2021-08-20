T = int(input())
for _ in range(T):
    (X, K) = [int(x) for x in input().split()]
    (x, y) = (2, 1)
    while x <= K:
        (x, y) = (x * 2, x)
    print(X / x * (1 + 2 * (K - y)))
