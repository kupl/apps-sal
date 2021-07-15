# cook your dish here
import heapq as hq
from math import sqrt

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

for _ in range(int(input())):
    input()
    n = int(input())
    points = {} #dict x_val : lists of y-values, each list in {points} contains points with the same x-value
    buff = []
    for _ in range(n):
        x,y = tuple(map(int, input().split()))
        if x in points:
            hq.heappush(points[x], y)
        else:
            q = [y]
            points[x] = q
    d = 0
    for i in points:
        hq._heapify_max(points[i])
    
    cur = (min(points), hq._heappop_max(points[min(points)]))
    while points:
        min_x, buff = min(points), points.pop(min(points))
        while buff:
            next_y = hq._heappop_max(buff)
            next_pt = (min_x, next_y)
            d += distance(cur, next_pt)
            cur = next_pt

    print("{:.2f}".format(round(d,2)))
    
    
