from collections import Counter
import math
import sys
sys.setrecursionlimit(10**7)
#from sys import stdin,stdout
#import random
#import heapq
#from queue import PriorityQueue
#from functools import lru_cache
# @lru_cache(maxsize=None) #for optimizing the execution time of callable objects/functions(placed above callable functions)
adj = [[] for i in range(100005)]


def dfs(node):
    mex = 0
    size = 1
    for i in adj[node]:
        temp = dfs(i)
        mex = max(mex, temp[0])
        size += temp[1]
    return [mex + size, size]


try:
    for _ in range(int(input())):
        n = int(input())
        for i in range(1, n + 1):
            adj[i].clear()
        arr = [int(i) for i in input().split()]
        for i in range(1, n):
            # print(arr[i-1])
            adj[arr[i - 1]].append(i + 1)
            # adj[i].append(arr[i-1])
        ans = dfs(1)
        print(ans[0])


except EOFError as e:
    print(e)
