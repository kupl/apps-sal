######################################################################
# Write your code here
from collections import defaultdict as df
import sys
input = sys.stdin.readline
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
# sys.setrecursionlimit(0x100000)
# Write your code here
def RI(): return [int(x) for x in sys.stdin.readline().strip().split()]
def rw(): return input().strip().split()
#import heapq
# heapq.heapify(li) heappush(li,4) heappop(li)
#import random
# random.shuffle(list)
#infinite = float('inf')
# )


def dfs(a, n):
    depth = [0] * n
    depth[a] = 0
    x = 1
    stack = [a]
    vis[a] = 1
    l = [0, 0]
    l[0] += 1
    # stackindex=0
    # print(stack)
    while(len(stack) != 0):

        p = stack.pop()
        # print(p)
        # stackindex-=1
        for i in adj[p]:
            if(vis[i] == 1):
                continue
            vis[i] = 1
            stack.append(i)
            # stackindex+=1
            depth[i] = depth[p] ^ 1
            l[depth[i]] += 1
        x = (x + 1) % 2
        # print(depth)
        # print(vis)
        # print("hi")
    # print(depth)
    # print(l)

    s = n // 2
    if(l[0] <= s):
        print(l[0])
        for i in range(n):
            if(depth[i] == 0):
                print(i + 1, end=" ")
    else:
        print(l[1])
        for i in range(n):
            if(depth[i] == 1):
                print(i + 1, end=" ")
    print("")


t = int(input())

adj = [[] for i in range(200010)]
vis = [0] * (200010)
for _ in range(t):
    n, m = RI()

    for i in range(n):
        adj[i].clear()
        vis[i] = 0
    for i in range(m):
        a, b = RI()
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)
   # print("hi",0)
    dfs(0, n)
