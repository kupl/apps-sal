MOD = 10 ** 9 + 7


def nCrModpDP(n, r, p):
    C = [0] * (n + 1)
    C[0] = 1
    for i in range(1, n + 1):
        j = min(i, r)
        while j > 0:
            C[j] = (C[j] + C[j - 1]) % p
            j -= 1
    return C[r]


def nCrModpLucas(n, r, p):
    if r == 0:
        return 1
    ni = int(n % p)
    ri = int(r % p)
    return nCrModpLucas(int(n / p), int(r / p), p) * nCrModpDP(ni, ri, p) % p


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    value = nCrModpLucas(n - 1, k - 1, MOD)
    ans = 1
    for x in range(1, n - 1):
        if n - x - 1 >= k - 1:
            temp1 = nCrModpLucas(n - x - 1, k - 1, MOD)
        else:
            temp1 = 0
        if x >= k - 1:
            temp2 = nCrModpLucas(x, k - 1, MOD)
        else:
            temp2 = 0
        ans = ans * arr[x] ** (value - temp2 - temp1) % MOD
    print(ans)
