# cook your dish here
import heapq
import math
for i in range(int(input())):
    n, a, b, x, y, z = list(map(int, input().split()))
    cntrbtns = list(map(int, input().split()))
    t = math.ceil((z - b) / y)
    sumy = a + x * (t - 1)
    if (sum(cntrbtns) * 2 + sumy) < z:
        print("RIP")
        continue
    c = 0
    for i in range(n):
        cntrbtns[i] = - cntrbtns[i]
    heapq.heapify(cntrbtns)
    ele = 0
    while True:
        if sumy >= z:
            print(c)
            break
        ele = heapq.heappushpop(cntrbtns, math.ceil(ele / 2))
        if ele == 0:
            print("RIP")
            break
        sumy -= ele
        c += 1
