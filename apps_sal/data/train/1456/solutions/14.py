"""
Created on Sun Dec 22 22:04:23 2019

@author: user
"""
import math


def ceil(n):
    if(int(n) == n):
        return int(n)
    else:
        return int(n) + 1


def compute(n):
    if(n == 0):
        return 0
    temp = int(math.log(n, 2)) + 1
    ans = ((n) * (n + 1)) // 2
    ans -= temp
    rr = 1
    while(n != 0):
        ans -= ceil(n / 2) * rr
        n = n // 2
        rr = rr * 2
    return ans


t = int(input())
for i in range(t):
    l, r = list(map(int, input().split()))
    ans = compute(r) - compute(l - 1)
    print(ans)
