import sys
import string
import cmath
import math

T = int(input())
for i in range(T):
 N,D = list(map(int, input().split()))
 A = list(map(int, input().split()))
 s = sum(A)
 ans=0
 if (s%N)==0:
  x = s/N
  for j in range(N-D):
   if A[j]<x:
    A[j+D] -= x-A[j]
    ans+=x-A[j]
    A[j] = x
   elif A[j]>x:
    A[j+D] += A[j]-x
    ans+=A[j]-x
    A[j] = x
  for j in range(N):
   if A[j]!=x:
    ans=-1
 else:
  ans=-1
 
 print(ans)

