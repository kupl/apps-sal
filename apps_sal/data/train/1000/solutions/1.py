from math import *
for i in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(ceil(n/min(arr)))
