from functools import reduce
from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    arr = [0] * 360

    for i in a:
        arr[i] = 1
    val = 0
    dif = []
    for i in range(0, 360):
        if(arr[i] == 1):
            dif.append(i - val)
            val = i
    dif[0] = 360 - (val - dif[0])
    dif.append(360)
    q = reduce(gcd, (dif))
    needed = 360 / q
    print(int(needed - n))
