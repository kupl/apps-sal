from collections import deque
(N, M) = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(M):
    (u, v, c) = list(map(int, input().split()))
    G[u - 1].append((v - 1, c))
    G[v - 1].append((u - 1, c))
newG = [[] for _ in range(N)]
done = [0] * N
ans = [0] * N
que = deque([0])
ans[0] = 1
while que:
    start = que.popleft()
    done[start] = 1
    for t in G[start]:
        (nex, c) = t
        if done[nex] == 1:
            continue
        else:
            newG[start].append((nex, c))
            que.append(nex)
            if ans[start] == c:
                ans[nex] = c % N + 1
            else:
                ans[nex] = c
for a in ans:
    print(a)
