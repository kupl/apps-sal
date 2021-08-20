(N, M) = map(int, input().split())
p = [0] + list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(M)]
li = [[] for i in range(N + 1)]
for i in range(M):
    li[xy[i][0]].append(xy[i][1])
    li[xy[i][1]].append(xy[i][0])
lis = [0] * (N + 1)
ma = 0
for i in range(1, N + 1):
    if lis[i] == 0:
        deque = [i]
        lis[i] = i
        ma = i
        while deque:
            x = deque.pop(0)
            for j in li[x]:
                if lis[j] == 0:
                    lis[j] = i
                    deque.append(j)
lit = [[] for i in range(ma)]
lif = [[] for i in range(ma)]
for i in range(1, N + 1):
    lit[lis[i] - 1].append(i)
    lif[lis[i] - 1].append(p[i])
ans = 0
for i in range(ma):
    ans += len(set(lit[i]) & set(lif[i]))
print(ans)
