from math import gcd

T = int(input())
ans = []

for _ in range(T):
 N = int(input())
 A = [int(i) for i in input().split()]

 # isGcd = False
 a = A[0]
 for i in range(1,N):
  a = gcd(a,A[i])

 if(a==1):
  ans.append(N)
 else:
  ans.append(-1)

for i in ans:
 print(i)

