import sys
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')
 
import math
import collections
from sys import stdin,stdout,setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9+7
    
T = int(stdin.readline())
# T = 1

for _ in range(T):
    # n = int(stdin.readline())
    n,k = list(map(int,stdin.readline().split()))
    a = list(map(int,stdin.readline().split()))
    # w = list(map(int,stdin.readline().split()))
    # q = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    # s = stdin.readline().strip('\n')
    p = [[0]]; p.append([0])
    for i in range(n):
        p[a[i]%2].append(i+1)
    p[0].append(n+1); p[1].append(n+1)
    res = [True, True]
    for j in range(2):
        for i in range(len(p[j])-1):
            if(p[j][i+1] - p[j][i] > k):
                res[j] = False
                break
    mn = 500000
    for j in range(2):
        if(not res[j]):
            continue
        i = 1; s = 0; m=0
        while(i<len(p[j])):
            if(p[j][i]-s > k):
                s = p[j][i-1]
                m += 1
            else:
                i += 1
        m += 1
        mn = min(mn,m)
    if(mn == 500000):
        print(-1)
    else:
        print(mn)
