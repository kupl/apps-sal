from collections import deque
import sys
import bisect
def input(): return sys.stdin.readline().rstrip()


n = int(input())
A = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1] * (n + 1)
visited[0] = 0
visited[1] = 1

d = deque()
d.append(1)
dp = [10**10] * (n + 1)
dp[0] = 0
dp[1] = A[1]
update_task = [() for _ in range(n + 1)]
update_task[1] = (1, 0)
while d:
    v = d[-1]
    if graph[v] == []:
        d.pop()
        index, atai = update_task[v]
        dp[index] = atai
    else:
        i = graph[v].pop()
        if visited[i] != -1:
            continue
        bis = bisect.bisect_left(dp, A[i])
        update_task[i] = (bis, dp[bis])
        dp[bis] = A[i]
        visited[i] = bisect.bisect_left(dp, 10**10 - 100) - 1
        d.append(i)

print(*visited[1:], sep="\n")
