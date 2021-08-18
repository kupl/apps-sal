from collections import defaultdict
import sys
S = input()
N = len(S)
if N == 3:
    if S[0] == S[1]:
        if S[1] == S[2]:
            print((1))
        else:
            print((6))
    else:
        if S[0] == S[2]:
            print((7))
        elif S[1] == S[2]:
            print((6))
        else:
            print((3))
    return
a = S[0]
t = 1
for i in range(N):
    if S[i] != a:
        t = 0
        break
if t == 1:
    print((1))
    return

mod = 998244353
M = 0
for s in S:
    if s == 'b':
        M += 1
    elif s == 'c':
        M += 2
    M %= 3
dp = []
for i in range(2):
    for k in range(3):
        for l in range(3):
            dp.append((i, k, l))
dd = [[[0] * 3 for i in range(3)] for i in range(2)]
for i in range(3):
    dd[0][i][i] = 1
for k in range(2, N + 1):
    nd = [[[0] * 3 for i in range(3)] for i in range(2)]
    for p in dp:
        con, moji, m = p
        n = dd[con][moji][m]
        # print(con,moji,m)
        if con == 0:
            for k in range(3):
                if moji == k:
                    nd[1][k][(m + k) % 3] += n
                    nd[1][k][(m + k) % 3] %= mod
                else:
                    nd[0][k][(m + k) % 3] += n
                    nd[0][k][(m + k) % 3] %= mod
        else:
            for k in range(3):
                nd[1][k][(m + k) % 3] += n
                nd[1][k][(m + k) % 3] %= mod
    # print(nd)
    dd = nd
flag = 1
for i in range(N - 1):
    if S[i] == S[i + 1]:
        flag = 0
ans = flag
for k in range(3):
    ans += dd[1][k][M]
    ans %= mod
print(ans)
