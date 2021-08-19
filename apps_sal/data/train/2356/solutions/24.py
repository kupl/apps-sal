(N, K) = map(int, input().split())
mat = [[0 for i in range(j + 1)] for j in range(N + 1)]


def tar(Num, Sum):
    if Num < Sum:
        return 0
    return mat[Num][Sum]


mat[1][1] = 1
MOD = 998244353
for i in range(1, N + 1):
    for j in range(1, i + 1)[::-1]:
        if i * j == 1:
            continue
        mat[i][j] = tar(i - 1, j - 1) + tar(i, 2 * j)
        mat[i][j] %= MOD
print(mat[N][K])
