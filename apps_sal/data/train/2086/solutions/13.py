from collections import deque
n, q = list(map(int, input().split()))

d = deque(list(map(int, input().split())))

cache = []

for i in range(n):
    a, b = d.popleft(), d.popleft()
    cache.append((a, b))

    if a > b:
        d.appendleft(a)
        d.append(b)
    else:
        d.appendleft(b)
        d.append(a)

a = list(d)


for _ in range(q):
    m = int(input())
    if m <= n:
        print(*cache[m - 1])
    else:
        m -= n + 1
        m %= n - 1
        print(a[0], a[m + 1])
