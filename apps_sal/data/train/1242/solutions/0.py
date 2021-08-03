from math import *
for t in range(int(input())):
    n = int(input())
    numberlist = list(map(int, input().split()))
    numberlist.sort()
    print(numberlist[0] * (len(numberlist) - 1))
