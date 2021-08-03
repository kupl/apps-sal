import sys
import math as mt
import bisect
input = sys.stdin.readline
# t=int(input())
t = 1


for _ in range(t):
    # n=int(input())
    # n,k=map(int,input().split())
    k, a, b = list(map(int, input().split()))
    # n,h=(map(int,input().split()))
    # l1=list(map(int,input().split()))
    # l2=list(map(int,input().split()))
    #mat=[[0 for j in range(c+1)] for i in range(r+1)]
    ans = k + 1
    ans1 = 1
    op1 = min(a - ans1, k)
    k -= op1
    if k > 0:
        ex = k // 2
        ans1 = (a + ex * (b - a))
        if k % 2 != 0:
            ans1 += 1
    print(max(ans, ans1))
