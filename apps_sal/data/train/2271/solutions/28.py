from collections import Counter, deque, defaultdict
n, m = map(int, input().split())
p = list(map(int, input().split()))
idx_lst = [0] * n
for i, x in enumerate(p):
    idx_lst[x - 1] = i
lst = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    lst[x - 1].append(y - 1)
    lst[y - 1].append(x - 1)
seen = [False] * n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    seen[i] = True
    q = deque([i])
    dic = defaultdict(int)
    dic[i] += 1
    while q:
        t = q.pop()
        for j in lst[t]:
            if seen[j]:
                continue
            seen[j] = True
            dic[j] += 1
            q.append(j)
    for k in list(dic.keys()):
        if dic[idx_lst[k]]:
            ans += 1
print(ans)
