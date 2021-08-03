import heapq
from math import ceil


for _ in range(int(input())):
    n, a, b, x, y, z = list(map(int, input().split()))
    c = [-int(i) for i in input().split()]
    heapq.heapify(c)
    days = ceil((z - b) / y)
    pig = z - a
    if ceil((pig + 2 * sum(c)) / x) >= days:
        print("RIP")
    else:
        ans = 0
        while ceil(pig / x) >= days and any(c):
            use = -heapq.heappop(c)
            pig -= use
            heapq.heappush(c, -(use >> 1))
            ans += 1
        if ceil(pig / x) >= days:
            print("RIP")
        else:
            print(ans)
