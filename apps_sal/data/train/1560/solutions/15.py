import math
import sys

def fun(n,x):
 res = 1
 for i in range(n, x,-1):
  res = (res*i)%1000000007
 return res

def degree(a,k):
 res = 1
 cur = a
 while(k):
  if (k % 2):
   res = (res * cur) % 1000000007
  k /= 2
  cur = (cur * cur) % 1000000007
 return res
 
def inv_fun(k):
 denom = 1
 for x in range(1, k+1, 1):
  denom = (denom*x) % 1000000007
 denom = degree(denom, 1000000005) % 1000000007
 return denom
  
def nCr(n,r):
 return fun(n,n-r)*inv_fun(r)
 
T = int(input())
for x in range(T):
 N, K = [int(y) for y in input().split(" ")]
 array = [int(t) for t in input().split(" ")]
 count = 0
 for i in range(len(array)):
  if(array[i] == 0):
   count += 1
 K = min(N,K)
 if count != 0:
  sum = 0
  for j in range(0,min(N-count,K)+1):
   sum += nCr(N-count,j)
   
 elif K%2 == 0:
  sum = 0
  for j in range(0,K+1,2):
   sum += nCr(N,j)
 else:
  sum = 0
  for j in range(1,K+1,2):
   sum += nCr(N,j)
 print(sum%1000000007)
