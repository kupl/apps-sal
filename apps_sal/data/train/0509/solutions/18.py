from collections import Counter, deque
(n, m) = map(int, input().split())
lst = [[] for _ in range(n)]
for i in range(m):
    (u, v, c) = map(int, input().split())
    lst[u - 1].append((v - 1, c))
    lst[v - 1].append((u - 1, c))
ans = [1] + [0] * (n - 1)
q = deque([0])
while q:
    x = q.pop()
    for (i, j) in lst[x]:
        if ans[i] != 0:
            continue
        if j == ans[x]:
            if j == n:
                ans[i] = 1
            else:
                ans[i] = j + 1
        else:
            ans[i] = j
        q.append(i)
print(*ans, sep='\n')
