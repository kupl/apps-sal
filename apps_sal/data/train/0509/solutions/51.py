from collections import deque

N, M = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = list(map(int, input().split()))
    u -= 1
    v -= 1
    Edge[u].append((v, c))
    Edge[v].append((u, c))

Ans = [-1] * N
Ans[0] = 1
Q = deque()
Q.append(0)

while Q:
    now = Q.popleft()
    for nex, color in Edge[now]:
        if Ans[nex] != -1:
            continue
        if color == Ans[now]:
            Ans[nex] = color + 1
            Q.append(nex)
        else:
            Ans[nex] = color
            Q.append(nex)
if -1 in Ans:
    print('No')
else:
    for ans in Ans:
        print(ans)

