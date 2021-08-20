from collections import deque
(n, d) = [int(i) for i in input().split()]
alist = [int(i) for i in input().split()]
de = deque()
i = 0
m = 0
while i < n:
    while i < n and (len(de) == 0 or alist[i] - de[0] <= d):
        de.append(alist[i])
        if len(de) >= 3:
            m += (len(de) - 1) * (len(de) - 2) // 2
        i += 1
    de.popleft()
print(m)
