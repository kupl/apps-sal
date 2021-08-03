import sys
import math
from collections import defaultdict, Counter

# input=sys.stdin.readline
# def print(x):
#     sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP3/output.txt",'w')
# sys.stdin=open("CP3/input.txt",'r')

# m=pow(10,9)+7
t = int(input())
for i in range(t):
    a, m = map(int, input().split())
    r = (m - 1) // a
    # print(r)
    l = []
    for j in range(1, r + 1):
        if m % (a * j + 1) == 0:
            d = m // (a * j + 1)
            l.append(d * j)
    print(len(l))
    print(*l)
