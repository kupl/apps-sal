import heapq
from math import ceil, floor
for _ in range(int(input())):
    (n, a, b, x, y, z) = map(int, input().split())
    s = [-int(i) for i in input().split()]
    days = floor((z - b) / y)
    current = a + days * x
    if b + days * y == z:
        z += 1
    count = 0
    heapq.heapify(s)
    while current < z:
        ret = heapq.heappop(s)
        ret = -ret
        if ret == 0:
            break
        else:
            current += ret
            heapq.heappush(s, -(ret // 2))
        count += 1
    print(count) if current >= z else print('RIP')
