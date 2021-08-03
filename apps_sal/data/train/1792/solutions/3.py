MOD = 12345787
FLAG = False
f = []


def prework(MAXN=10000):
    nonlocal FLAG
    nonlocal f
    if FLAG:
        return
    FLAG = True
    f = [[[0, 0] for j in range(8)] for i in range(MAXN + 2)]
    # f[i][j][k], k -> already use hole
    f[0][7][0] = 1
    for i in range(MAXN + 1):
        for j in range(7):
            for k in range(3):
                if ((j >> k) & 1) == 0:
                    f[i][j | (1 << k)][1] += f[i][j][0]
        for j in range(8):
            for k in range(2):
                f[i][j][k] %= MOD
        for k in range(2):
            # f[i][*][k] -> f[i+1][?][k]
            f[i + 1][7][k] += f[i][0][k]
            f[i + 1][1][k] += f[i][0][k]
            f[i + 1][4][k] += f[i][0][k]
            f[i + 1][0][k] += f[i][1][k]
            f[i + 1][6][k] += f[i][1][k]
            f[i + 1][5][k] += f[i][2][k]
            f[i + 1][4][k] += f[i][3][k]
            f[i + 1][3][k] += f[i][4][k]
            f[i + 1][0][k] += f[i][4][k]
            f[i + 1][2][k] += f[i][5][k]
            f[i + 1][1][k] += f[i][6][k]
            f[i + 1][0][k] += f[i][7][k]


def three_by_n(n):
    prework()
    return f[n + 1][0][n % 2] % MOD
