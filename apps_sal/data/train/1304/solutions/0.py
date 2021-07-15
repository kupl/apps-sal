import sys
# import math as mt
# from collections import Counter
# from itertools import permutations
# from functools import reduce
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

# sys.setrecursionlimit(10**7)
# INF = float('inf')
# MOD1, MOD2 = 10**9+7, 998244353

n, k = get_ints()

for _ in range(k):
    
    arr = get_array()
    
    for i in reversed(range(n-1)):
        
        if arr[i] < arr[i+1]:
            
            ind = i+1
            minn = arr[i+1]
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    minn = min(arr[j], minn)
                    ind = j
                    
            arr[i], arr[ind] = arr[ind], arr[i]
            
            arr = arr[:i+1] + sorted(arr[i+1:])
            
            break
    
    print(*arr)
