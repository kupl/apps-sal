# cook your code here
N=int(input())
A=[0 for _ in range(N+1)]
B=[int(x) for x in input().split()]
for x in B:
 A[x]=1
for i in range(N+1):
 if A[i] == 0:
  print(i, end=' ')
