from collections import deque
N, M = list(map(int, input().split()))
c, to = dict(), [[] for _ in range(N)]

def maxmin(x, y):
    if x < y:
        x, y = y, x
    return (x,y)

for i in range(M):
    x,y,z = list(map(int, input().split()))
    x,y = x-1,y-1
    x,y = maxmin(x,y)
    if (x,y) not in c:
        c[(x,y)] = z
        to[x].append(y)
        to[y].append(x)

q = deque([0])
mark = [0] * N
mark[0] = 1
while q:
    now = q.popleft()
    for next in to[now]:
        if mark[next]:
            continue
        cost = c[maxmin(now, next)]
        if mark[now] == cost:
            mark[next] = mark[now] % N + 1
        else:
            mark[next] = cost
        q.append(next)

for i in mark:
    print(i)

