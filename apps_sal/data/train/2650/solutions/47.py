from sys import stdin, stdout
from time import perf_counter

import sys
sys.setrecursionlimit(10**9)
mod = 10**9 + 7

# import sys
# sys.stdout = open("e:/cp/output.txt","w")
# sys.stdin = open("e:/cp/input.txt","r")

n, l = map(int, input().split())
a = [input() for item in range(n)]
b = sorted(a)
print(''.join(b))
