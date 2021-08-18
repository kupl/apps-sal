import itertools

S = input()
N = len(S)
if all(S[0] == c for c in S):
    print((1))
    return
if N == 2:
    print((1 if S[0] == S[1] else 2))
    return

if N == 3:
    def another(a, b):
        s = set('abc')
        s -= set([a, b])
        return list(s)[0]
    ptn = set()
    stack = [S]
    while stack:
        a = stack.pop()
        ptn.add(a)
        if a[0] != a[1]:
            b = another(a[0], a[1]) * 2 + a[2]
            if not b in ptn:
                stack.append(b)
        if a[1] != a[2]:
            c = a[0] + another(a[1], a[2]) * 2
            if not c in ptn:
                stack.append(c)
    print((len(ptn)))
    return

#N >= 4
MOD = 998244353
dp = [[[0 for u in range(2)] for l in range(3)] for s in range(3)]
# dp[sum%3][last][exist'xx'?]
for ptn in itertools.product(list(range(3)), repeat=4):
    seq = (ptn[0] == ptn[1] or ptn[1] == ptn[2] or ptn[2] == ptn[3])
    dp[sum(ptn) % 3][ptn[3]][seq] += 1

for n in range(4, N):
    dp2 = [[[0 for u in range(2)] for l in range(3)] for s in range(3)]
    for s in range(3):
        for l in range(3):
            for u in range(2):
                for l2 in range(3):
                    s2 = (s + l2) % 3
                    u2 = u or l == l2
                    dp2[s2][l2][u2] += dp[s][l][u]
                    dp2[s2][l2][u2] %= MOD
    dp = dp2

sm = 0
for c in S:
    sm += ord(c) - ord('a')
seq = False
for c1, c2 in zip(S, S[1:]):
    if c1 == c2:
        seq = True
        break
ans = sum([dp[sm % 3][i][1] for i in range(3)])
if not seq:
    ans += 1
print((ans % MOD))
