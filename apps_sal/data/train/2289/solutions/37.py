# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#n, = map(int,readline().split())
s = input()


def next_index(N, s):
    D = [-1] * 26
    E = [None] * (N + 1)
    cA = ord('a')
    for i in range(N - 1, -1, -1):
        E[i + 1] = D[:]
        D[ord(s[i]) - cA] = i
    E[0] = D
    return E


n = len(s)
nxt = next_index(n, s)

"""
for i in nxt:
    print(i[:4])
"""

# print(nxt)
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    idx = max(nxt[i])
    bad = min(nxt[i])
    dp[i] = dp[idx + 1] + 1 if bad != -1 else 0

# print(nxt[0])
# print(dp)

k = dp[0] + 1
ans = [None] * k

v = 0
for i in range(k):
    # print(v)
    if v == n:
        ans[-1] = 0
        break

    for j in range(26):
        #print(nxt[v+1][j], dp[nxt[v+1][j]])
        if nxt[v][j] == -1 or dp[nxt[v][j] + 1] < dp[v]:
            ans[i] = j
            v = nxt[v][j] + 1
            break

# print(ans)


def f(x):
    return chr(x + ord("a"))


a = "".join(map(f, ans))
print(a)


"""
x = [chr(ord("z")-i) for i in range(26)]
x = "".join(x)
print(x)
"""
