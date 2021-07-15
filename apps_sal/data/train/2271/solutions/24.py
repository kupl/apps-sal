from collections import deque

n,m = map(int,input().split())

p = list(map(int,input().split()))

root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

check = [-1]*n

for j in range(n):
    if check[j] != -1:
        continue
    stack=deque([j])
    check[j] = j
    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i]=j
                stack.append(i)

ans = 0
for key, value in enumerate(p):
    if check[key] == check[value-1]:
        ans += 1
print(ans)
