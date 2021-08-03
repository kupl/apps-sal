import sys
import math
import heapq


def half(arr):
    for i in range(len(arr)):
        arr[i] //= 2
    return arr


def main(arr, m):
    x, y, z = arr
    x.sort()
    y.sort()
    z.sort()

    while m != 0:

        a, b, c = x[-1], y[-1], z[-1]

        s = max(a, b, c)

        if s == a:
            half(x)
        elif s == b:
            half(y)
        else:
            half(z)
        m -= 1
    return max(x[-1], y[-1], z[-1])


for i in range(int(input())):
    r, g, b, m = list(map(int, input().split()))
    arr = []
    for j in range(3):
        c = list(map(int, input().split()))
        arr.append(c)

    print(main(arr, m))
