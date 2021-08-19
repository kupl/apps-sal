import sys
readline = sys.stdin.readline
S = list([ord(x) - 97 for x in readline().strip()])
N = len(S)
table = [[0] * 26 for _ in range(N)]
for i in range(N):
    table[i][S[i]] = 1
for i in range(1, N):
    for j in range(26):
        table[i][j] += table[i - 1][j]
Q = int(readline())
Ans = [None] * Q
for qu in range(Q):
    (l, r) = list(map(int, readline().split()))
    l -= 1
    r -= 1
    if l == r or S[l] != S[r]:
        Ans[qu] = True
        continue
    K = [table[r][j] - table[l][j] for j in range(26)]
    if len([k for k in K if k]) <= 2:
        Ans[qu] = False
    else:
        Ans[qu] = True
print('\n'.join(['Yes' if s else 'No' for s in Ans]))
