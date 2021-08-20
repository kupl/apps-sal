from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
g = [[] for i in range(n)]
for (x, y, z) in a:
    g[x - 1].append((y - 1, z))
    g[y - 1].append((x - 1, z))


def tree(s):
    ans = [0] * n
    ans[s] = 1

    def bfs():
        d = deque()
        d.append(s)
        while len(d):
            x = d.popleft()
            for i in range(len(g[x])):
                y = g[x][i][0]
                if ans[y] == 0:
                    d.append(y)
                    if ans[x] == g[x][i][1]:
                        if ans[x] == n:
                            ans[y] = n - 1
                        else:
                            ans[y] = ans[x] + 1
                    else:
                        ans[y] = g[x][i][1]
        return ans
    return bfs()


v = tree(0)
for i in v:
    print(i)
