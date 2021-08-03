import bisect

s = input()
n = len(s)
ans = 0
ptn = [[0] * (n + 1) for i in range(4)]

for i in range(1, 5):
    for j in range(n):
        if j + 2 * i >= n:
            break
        if s[j] == s[j + i] and s[j + i] == s[j + 2 * i]:
            ptn[i - 1][j + 1] = 1
    for j in range(n):
        ptn[i - 1][j + 1] += ptn[i - 1][j]

ans = 0
for l in range(n):
    tmp_ans = 1000000
    for i in range(4):
        tmp = bisect.bisect_left(ptn[i], ptn[i][l] + 1)
        tmp_ans = min(tmp_ans, tmp - 1 + 2 * (i + 1))
    ans += max(0, n - tmp_ans)
print(ans)
