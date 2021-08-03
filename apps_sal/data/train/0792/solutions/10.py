T = int(input())
for _ in range(T):
    N, S = input().split()
    N = int(N)
    M = len(S)
    mod = (10**9) + 7
    if M >= N:
        print(0)
    else:
        f = pow(26, (N - M), mod)
        g = M * 25 * (pow(26, (N - M - 1), mod))
        print((f + g) % mod)
