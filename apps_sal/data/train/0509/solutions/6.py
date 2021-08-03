from collections import deque
import copy
import sys
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
g = [[] for i in range(n)]

for x, y, z in a:
    g[x - 1].append((y - 1, z))
    g[y - 1].append((x - 1, z))


def tree(s):

    INF = -10**9
    dis = [INF for i in range(n)]
    ans = [0] * n
    dis[s] = 0
    ans[s] = 1

    def bfs():
        d = deque()
        d.append(s)

        while len(d):
            x = d.popleft()

            for i in range(len(g[x])):
                y = g[x][i][0]
                if dis[y] == INF:
                    d.append(y)
                    dis[y] = dis[x] + 1
                    if ans[y] == 0:
                        if ans[x] == g[x][i][1]:
                            if ans[x] == n:
                                ans[y] = n - 1
                            else:
                                ans[y] = copy.copy(ans[x]) + 1
                        else:
                            ans[y] = copy.copy(g[x][i][1])

        return ans
    return bfs()


v = tree(0)
for i in v:
    print(i)
