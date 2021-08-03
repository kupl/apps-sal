#!/bin/python
tc = int(input())
while tc:
    tc -= 1
    n = int(input())
    ans = 2**(n - 2)
    ans += 1
    print(ans)
