mod = 998244353
f0 = [[0 for i in range(11)] for j in range(2010)]
f1 = [[0 for i in range(11)] for j in range(2010)]
fac = [0 for i in range(2010)]
tab = [0 for i in range(11)]
C = [[0 for i in range(2010)] for j in range(2010)]


def Init():
    fac[0] = 1
    for i in range(2010):
        if i > 0:
            fac[i] = fac[i - 1] * i % mod
        C[i][0] = 1
        for j in range(1, 2010):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod


def len(x):
    res = 0
    while x > 0:
        res += 1
        x = x // 10
    return res


def solve():
    n = int(input())
    f0[0][0] = f1[0][0] = 1
    a = list(map(int, input().split()))
    c0, c1 = 0, 0
    s0, s1 = 0, 0
    for nu in a:
        m = nu % 11
        if len(nu) & 1:
            c1 += 1
            s1 += m
            for i in range(11):
                f1[c1][i] = 0
            for i in range(c1 - 1, -1, -1):
                for j in range(11):
                    if f1[i][j] == 0:
                        continue
                    f1[i + 1][(j + m) % 11] += f1[i][j]
                    f1[i + 1][(j + m) % 11] %= mod
        else:
            c0 += 1
            s0 += m
            for i in range(11):
                f0[c0][i] = 0
            for i in range(c0 - 1, -1, -1):
                for j in range(11):
                    if f0[i][j] == 0:
                        continue
                    f0[i + 1][(j + m) % 11] += f0[i][j]
                    f0[i + 1][(j + m) % 11] %= mod
    s1 %= 11
    s0 %= 11
    part = c1 // 2
    for i in range(11):
        tab[i] = 0
    for i in range(11):
        tab[(i + i + 11 - s1) % 11] = f1[c1 - part][i]
    for i in range(11):
        tab[i] = tab[i] * fac[part] % mod * fac[c1 - part] % mod

    ans = 0
    if c1 == 0:
        ans = f0[c0][0] * fac[c0]
    elif c0 == 0:
        ans = tab[0]
    else:
        for i in range(c0 + 1):
            for j in range(11):
                if f0[i][j] == 0:
                    continue
                # print(f0[i][j], tab[(j + j + 11 - s0) % 11] \
                # , fac[i] % mod * fac[c0 - i] % mod, C[j + (c1 - part) - 1][(c1 - part) - 1] % mod * C[part + c0 - i][part] % mod )
                ans = (ans +
                       fac[i] % mod * fac[c0 - i] % mod *
                        f0[i][j] * tab[(j + j + 11 - s0) % 11] % mod *
                        C[i + (c1 - part) - 1][(c1 - part) - 1] % mod *
                       C[part + c0 - i][part]
                       ) % mod
    print(ans)


Init()
T = int(input())
for ttt in range(T):
    solve()
