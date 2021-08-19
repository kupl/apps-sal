from collections import defaultdict
import os
import sys
from io import BytesIO, IOBase


def binarySearchCount(arr, n, key):
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] <= key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def can_break(N, a, d, x, y, maxi, mini):
    c = x + y
    if c < mini:
        return 0
    if c in d:
        return -1
    if c > maxi:
        return N
    x = binarySearchCount(a, N, c)
    return x
    '\n    mid=(N-1)//2\n    if c<a[mid]:\n     count=0\n     for i in a:\n      if i>c:\n       return count\n      count+=1\n  \n    else:\n     count=mid+1\n     for i in range(mid+1,N):\n      if a[i]>c:\n       return count\n      count+=1\n    '


T = int(input())
while T:
    N = int(input())
    a = tuple(map(int, input().split()))
    d = defaultdict()
    mini = a[0]
    maxi = a[-1]
    for i in range(N):
        d[a[i]] = i
    Q = int(input())
    while Q:
        (x, y) = list(map(int, input().split()))
        if x == 0 and y == 0:
            print(0)
        else:
            print(can_break(N, a, d, x, y, maxi, mini))
        Q -= 1
    T -= 1
