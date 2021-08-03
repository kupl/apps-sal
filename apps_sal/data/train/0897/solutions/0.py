# cook your dish here
# cook your dish here
MOD = 10 ** 9 + 7

for t in range(int(input())):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    I, D = [0] * (N + 2), [0] * (N + 2)
    for i in range(M):
        x, L, R = input().split()
        L, R = int(L), int(R)
        if x == 'I':
            I[L] += 1
            I[R] -= 1
        else:
            D[L] += 1
            D[R] -= 1

    impossibru = mx = mn = 0
    ans = 1
    for i in range(N):
        I[i] += I[i - 1]
        D[i] += D[i - 1]
        if I[i] and D[i]:
            impossibru = 1
            break
        if not I[i] and not D[i]:
            ans = ans * (mx - mn + 1) % MOD
            mn, mx = 1, K
        elif I[i]:
            mx = min(mx + 1, K)
            mn += 1
        elif D[i]:
            mn = max(1, mn - 1)
            mx -= 1
        if mn > mx:
            impossibru = 1
            break
        if A[i] != -1:
            if not mn <= A[i] <= mx:
                impossibru = 1
                break
            mn = mx = A[i]
    ans = ans * (mx - mn + 1) % MOD

    print(0 if impossibru else ans)
