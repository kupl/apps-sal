import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
S = list(map(lambda x: ord(x) - ord('a'), list(input())[:-1]))
table = [[] for _ in range(26)]
for i in range(len(S)):
    x = S[i]
    table[x].append(i + 1)
for c in range(26):
    table[c].append(len(S) + 1)
dp = [len(S)] * (len(S) + 2)
dp[-1] = 0
rev = [0] * (len(S) + 1)
revc = [0] * (len(S) + 1)
for i in range(len(S) - 1, -1, -1):
    for x in range(26):
        j = table[x][bl(table[x], i + 1)]
        if dp[i] > dp[j] + 1:
            dp[i] = dp[j] + 1
            rev[i] = j
            revc[i] = x
x = 0
res = []
while x < len(S):
    c = revc[x]
    res.append(chr(c + ord('a')))
    if x == len(S):
        break
    x = rev[x]
print(''.join(res))
