from heapq import *
n = int(input())
turn = [99 ** 9]
opty = 0
for (i, a) in enumerate(map(int, input().split())):
    a -= i
    optx = -turn[0]
    if optx <= a:
        heappush(turn, -a)
    else:
        heappush(turn, -a)
        heappop(turn)
        heappush(turn, -a)
        opty += optx - a
print(opty)
