from collections import deque
n, q = list(map(int, input().split()))
a = deque(list(map(int, input().split())))
b = []
m = a.index(max(a))
for i in range(m):
    a0, a1 = a.popleft(), a.popleft()
    b.append([a0, a1])
    if a0 < a1:
        a0, a1 = a1, a0
    a.appendleft(a0)
    a.append(a1)
for i in range(q):
    c = int(input())
    if c <= m:
        print('{} {}'.format(b[c-1][0], b[c-1][1]))
    else:
        c -= m+1
        c %= n-1
        print('{} {}'.format(a[0], a[c+1]))

