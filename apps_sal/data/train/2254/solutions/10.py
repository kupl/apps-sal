import collections
(n, q) = map(int, input().split())
dq = collections.deque()
l = n * [0]
p = list(l)
ans = 0
t = 0
ansl = []
while q:
    (a, b) = map(int, input().split())
    if a == 1:
        dq.append(b - 1)
        (l[b - 1], p[b - 1]) = (l[b - 1] + 1, p[b - 1] + 1)
        ans = ans + 1
    elif a == 2:
        ans = ans - l[b - 1]
        l[b - 1] = 0
    else:
        while b > t:
            t = t + 1
            j = dq.popleft()
            p[j] = p[j] - 1
            if l[j] > p[j]:
                l[j] = l[j] - 1
                ans = ans - 1
    ansl.append(str(ans))
    q = q - 1
print('\n'.join(ansl))
