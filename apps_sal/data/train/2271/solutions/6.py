from collections import deque
(N, M) = map(int, input().split())
plist = list(map(int, input().split()))
pilist = []
for (i, p) in enumerate(plist):
    pilist.append((p, i + 1))
pilist.sort(key=lambda x: x[0])
dic = {k: [] for k in range(N + 1)}
for _ in range(M):
    (x, y) = map(int, input().split())
    dic[plist[x - 1]].append(plist[y - 1])
    dic[plist[y - 1]].append(plist[x - 1])
groups = []
done = [0] * (N + 1)
for p in range(1, N + 1):
    if done[p] == 0:
        done[p] = 1
        group_p = [p]
        group_i = [pilist[p - 1][1]]
        queue = deque([p])
        while queue:
            q = queue.pop()
            for q_n in dic[q]:
                if done[q_n] == 0:
                    done[q_n] = 1
                    group_p.append(q_n)
                    group_i.append(pilist[q_n - 1][1])
                    queue.append(q_n)
        groups.append((group_p, group_i))
ans = 0
for group in groups:
    p = set(group[0])
    i = set(group[1])
    ans += len(p & i)
print(ans)
