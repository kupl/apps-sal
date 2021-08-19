import sys
from math import log2
from itertools import combinations
for _ in range(int(sys.stdin.readline())):
    n = str(sys.stdin.readline())
    n = n[:-1]
    temp = 0
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            temp = 1
    if temp:
        print(1)
    else:
        print(0)
