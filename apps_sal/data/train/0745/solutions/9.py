"""
Created on Thu Dec 19 19:45:35 2019

@author: user
"""


def ceil(num, arr, l, r):
    if(l > r):
        return r + 1
    if(arr[r] < num):
        return r + 1
    while(l < r):
        m = (l + r) // 2
        if(arr[m] >= num):
            r = m
        else:
            l = m + 1
    return r


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    l = [0 for i in range(n)]
    r = [0 for i in range(n)]
    l[0] = 1
    r[-1] = 1
    for i in range(1, n):
        l[i] = min(l[i - 1] + 1, arr[i])
        r[n - 1 - i] = min(r[n - i] + 1, arr[n - 1 - i])
    counter = -1
    for i in range(n):
        counter = max(counter, min(l[i], r[i]))
    print(sum(arr) - counter**2)
