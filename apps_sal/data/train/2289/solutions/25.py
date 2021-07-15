import sys
input = sys.stdin.readline

a = list(input().rstrip())
n = len(a)
x = [[0] * 26 for _ in range(n + 1)]
for i in range(n):
    j = ord(a[i]) - 97
    x[i][j] = i + 1
for i in range(n - 1, -1, -1):
    for j in range(26):
        if x[i][j] == 0:
            x[i][j] = x[i + 1][j]
minlen = [0] * (n + 1)
minalph = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    l = 114514
    for j in range(26):
        if x[i][j] == 0:
            l, m = 0, j
            break
        if l > minlen[x[i][j]] + 1:
            l, m = minlen[x[i][j]] + 1, j
    minlen[i] = l
    minalph[i] = m
ans = []
i = 0
for _ in range(minlen[0] + 1):
    ans.append(chr(minalph[i] + 97))
    i = x[i][minalph[i]]
ans = "".join(ans)
print(ans)
