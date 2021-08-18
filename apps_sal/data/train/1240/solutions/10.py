import sys
from math import log2
from itertools import combinations


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    lis = list(map(int, sys.stdin.readline().split()))
    for i in range(len(lis)):
        if lis[i] % 6 == 0:
            lis[i] = 6
        else:
            lis[i] = lis[i] % 6
    print(sum(lis))
