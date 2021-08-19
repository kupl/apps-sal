from collections import defaultdict, deque

n = int(input())
adj = [[] for _ in range(n)]
v = [0] * n
l = list(map(int, input().split()))
for i, f in enumerate(l):
    adj[f - 1].append(i + 1)

s = list(map(int, input().split()))

Q = deque([(0, s[0], s[0])])
ans = 0
flag = False
possible = True
while Q and possible:
    # print(Q)
    flag = not flag
    for _ in range(len(Q)):
        cur, v, curs = Q.popleft()
        if v < 0:
            possible = False
            ans = -1
            break
        ans += v
        if flag:
            for i in adj[cur]:
                if len(adj[i]) <= 1:
                    Q.append((i, 0, curs))
                else:
                    temp = min([s[k] for k in adj[i]])
                    Q.append((i, temp - curs, temp))
        else:
            for i in adj[cur]:
                Q.append((i, s[i] - curs, s[i]))
print(ans)
