s = input()
hs = [[0] * 3 for i in range(len(s) + 1)]
for i in range(len(s)):
    for j in range(3):
        hs[i + 1][j] = hs[i][j]
    if s[i] == 'x':
        hs[i + 1][0] += 1
    if s[i] == 'y':
        hs[i + 1][1] += 1
    if s[i] == 'z':
        hs[i + 1][2] += 1
n = int(input())
res = []
for i in range(n):
    (l, r) = list(map(int, input().split(' ')))
    t = [hs[r][i] - hs[l - 1][i] for i in range(3)]
    res.append('YES' if r - l < 2 or max(t) - min(t) < 2 else 'NO')
print('\n'.join(res))
