from collections import deque
(n, q) = map(int, input().split())
a = deque((int(i) for i in input().split()))
Mmax = max(a)
ans = {}
index = 0
while True:
    first = a.popleft()
    second = a.popleft()
    if first == Mmax:
        a.appendleft(second)
        a.appendleft(first)
        break
    else:
        a.append(min(first, second))
        a.appendleft(max(first, second))
        index += 1
        ans[index] = (first, second)
M = a.popleft()
now = list(a)
for i in range(q):
    x = int(input())
    if x <= index:
        print(*ans[x])
    else:
        x -= index
        print(M, now[x % len(now) - 1])
