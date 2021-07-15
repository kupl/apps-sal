import sys

n = int(input())
sys.setrecursionlimit(100*1000+100)

ch = [[] for _ in range(n)]
for i, x in enumerate(map(int, input().split(' ')), start=1):
    ch[x-1].append(i)

s = list(map(int, input().split(' ')))

ans = 0
def dfs(v, buf):
    nonlocal ans
    while True:
        m = min((s[c] for c in ch[v]), default=buf) if s[v] == -1 else s[v]
        if m < buf: ans = -1
        if ans == -1: return
        ans += m - buf
        if len(ch[v]) == 1:
            v = ch[v][0]
            buf = m
            continue
        else:
            for c in ch[v]: 
                dfs(c, m)
            break

dfs(0, 0)
print (ans)
