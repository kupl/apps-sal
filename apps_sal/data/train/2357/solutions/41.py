def nCr(n, r):
    A = B = 1
    for _ in range(r):
        A *= n
        A %= Mod
        B *= r
        B %= Mod
        n -= 1
        r -= 1
    return A * pow(B, Mod - 2, Mod) % Mod


(N, M) = map(int, input().split())
A = list(map(int, input().split()))
Mod = 10 ** 9 + 7
print(nCr(M + N, sum(A) + N))
