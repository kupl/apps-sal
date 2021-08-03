n, *d = map(int, open(0).read().split())
z = {j: i for i, j in enumerate(d)}
*s, = sorted(d)
P = [-1] * n
S = {i: 1 for i in d}
D = {i: 0 for i in d}
ok = 1
for v in s[n - 1:0:-1]:
    p = v - n + 2 * S[v]
    if p >= v:
        ok = 0
    if p in z:
        S[p] += S[v]
        D[p] += D[v] + S[v]
        P[z[v]] = z[p]
    else:
        ok = 0
if ok and D[s[0]] == s[0]:
    for i, pi in enumerate(P):
        if pi != -1:
            print(i + 1, pi + 1)
else:
    print(-1)
