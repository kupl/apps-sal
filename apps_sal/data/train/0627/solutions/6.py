# cook your dish here
# import sys
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

import math
import collections
from sys import stdin,stdout,setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9+7

def nCrModp(n, r, p): 
 if (r > n- r): 
  r = n - r 
 C = [0 for i in range(r + 1)] 
 
 C[0] = 1
 
 for i in range(1, n + 1): 
  for j in range(min(i, r), 0, -1): 
   C[j] = (C[j] + C[j-1]) % p 
 
 return C[r] 
 

# T = int(stdin.readline())
# for _ in range(T):
 # n = int(stdin.readline())
n,k = list(map(int,stdin.readline().split()))
 # a = list(map(int,stdin.readline().split()))
 # q = list(map(int,stdin.readline().split()))
 # b = list(map(int,stdin.readline().split()))
 # a = stdin.readline().strip('\n')
N = n+k-1
R = n-1
print(nCrModp(N,R,M))
