for i in range(int(input())):
    L = input().split()
    N = int(L[0])
    S = (L[1])
    Q = N - len(S)
    ans = 0
    if N > len(S):
        ans = pow(26, Q - 1, (10**9 + 7))
        ans *= (26 + 25 * len(S))

        ans = ans % (10**9 + 7)
    print(ans)
