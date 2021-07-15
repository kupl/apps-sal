from collections import deque
import bisect
import sys

sys.setrecursionlimit(200000)

N = int(input())
a = list(map(int, input().split()))
uvs = [list(map(int, input().split())) for _ in range(N-1)]
shortest = [10e+10 for _ in range(N)]
shortest[0] = 0

routes = [[] for _ in range(N)]

for uv in uvs:
    routes[uv[0]-1].append(uv[1]-1)
    routes[uv[1]-1].append(uv[0]-1)

lis = [10e+100 for _ in range(N)]
minimum = [10e+100 for _ in range(N)]
seen = [False for _ in range(N)]
seen[0] = True

def function(checking):
    insert_posi = bisect.bisect_left(lis, a[checking])
    preserved = lis[insert_posi]
    lis[insert_posi] = a[checking]
    minimum[checking] = bisect.bisect_left(lis, 10e+50)
    for route in routes[checking]:
        if seen[route] == False:
            seen[route] = True
            shortest[route] = shortest[checking]+1
            function(route)
    lis[insert_posi] = preserved
    return
        
function(0)

[print(x) for x in minimum]
