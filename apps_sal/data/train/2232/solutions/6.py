#!/usr/bin/env python3
import math
n = int(input())
x = 2
k = 1
while k <= n:
    assert x % k == 0
    y = ((k+1) * k) ** 2
    assert x <= y and (y - x) % k == 0
    assert (y - x) // k <= 10**18
    print((y - x) // k)
    x = (k+1) * k
    k += 1

