for T in range(int(input())):
    N, K = map(int, input().split())
    L = list(map(int, input().split()))

    m = max(L) + K
    s = min(L) - K

    print(m - s)
