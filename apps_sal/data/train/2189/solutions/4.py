
from sys import stdin
import heapq

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    q = []
    for i in a:
        heapq.heappush(q, -1 * i)

    f = 0
    g = 0

    while True:

        if len(q) == 0:
            print("HL")
            break

        f = heapq.heappop(q)
        f += 1
        if g != 0:
            heapq.heappush(q, g)

        if len(q) == 0:
            print("T")
            break
        g = heapq.heappop(q)
        g += 1
        if f != 0:
            heapq.heappush(q, f)
