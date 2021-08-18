import heapq
from math import ceil
for i in range(int(input())):
    n, a, b, x, y, z = list(map(int, input().split()))
    cntrbtns = [-(int(x)) for x in input().split()]

    if b >= z:
        print("RIP")
        continue
    sum = a + x * (ceil((z - b) / y) - 1)
    c = 0
    heapq.heapify(cntrbtns)
    ele = 0
    while sum < z and any(cntrbtns):
        ele = -heapq.heappop(cntrbtns)
        sum += ele
        heapq.heappush(cntrbtns, -(ele >> 1))
        c += 1
    print(["RIP", c][sum >= z])
