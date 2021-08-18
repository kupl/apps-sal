
def compute_nCr(n, r):
    C[0][0] = 1
    for i in range(1, n + 1):
        C[i][0] = 1
        for j in range(1, min(i, r) + 1):
            if i != j:
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
            else:
                C[i][j] = 1


def solve(n, m):
    store = [C[m + i - 1][i] for i in range(m + 1)]

    for i in range(1, n + 1):
        s = 1
        for j in range(1, m + 1):
            s = (s + store[j]) % MOD
            store[j] = (s * C[m + j - 1][j]) % MOD

    return s


MOD = 1000000000
LIMIT = 2000

C = [[0 for x in range(LIMIT + 1)] for y in range(2 * LIMIT + 1)]
compute_nCr(2 * LIMIT, LIMIT)
t = int(input())

while t:
    n, m = list(map(int, input().split()))
    print(solve(n, m))
    t -= 1
