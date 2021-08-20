import heapq
from math import ceil
for _ in range(int(input())):
    (n, a, b, x, y, z) = [int(i) for i in input().split()]
    A = [-int(i) for i in input().split()]
    heapq.heapify(A)
    days = ceil((z - b) / y)
    pig = z - a
    if ceil((pig + 2 * sum(A)) / x) >= days:
        print('RIP')
    else:
        ans = 0
        while ceil(pig / x) >= days and any(A):
            use = -heapq.heappop(A)
            pig -= use
            heapq.heappush(A, -(use >> 1))
            ans += 1
        print(['RIP', ans][ceil(pig / x) < days])
