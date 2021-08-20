import heapq
import math
for i in range(int(input())):
    (n, a, b, x, y, z) = list(map(int, input().split()))
    cntrbtns = list(map(int, input().split()))
    if b >= z:
        print('RIP')
        continue
    t = math.ceil((z - b) / y)
    sum = a + x * (t - 1)
    c = 0
    for i in range(n):
        cntrbtns[i] = -cntrbtns[i]
    heapq.heapify(cntrbtns)
    ele = 0
    while True:
        if sum >= z:
            print(c)
            break
        ele = -ele
        ele = heapq.heappushpop(cntrbtns, -(ele // 2))
        if ele == 0:
            print('RIP')
            break
        sum -= ele
        c += 1
