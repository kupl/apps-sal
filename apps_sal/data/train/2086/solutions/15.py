from collections import deque
n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
m = max(a)
dq = deque()
for i in a:
    dq.append(i)
ans = []
while dq[0] != m:
    x = dq.popleft()
    y = dq.popleft()
    ans.append((x, y))
    if x > y:
        dq.appendleft(x)
        dq.append(y)
    else:
        dq.appendleft(y)
        dq.append(x)
temp = list(dq)[1:]
for _ in range(q):
    x = int(input())
    if x <= len(ans):
        print(*ans[x - 1])
    else:
        print(m, temp[(x - len(ans) - 1) % len(temp)])
# print(ans)
