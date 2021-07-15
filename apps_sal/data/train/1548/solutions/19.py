# cook your dish here
T=int(input())
for _ in range(T):
 n=int(input())
 A=list(map(int,input().split()))
 for i in range(1,n):
  A[i]=min(A[i],A[i-1]+1)
 for i in range(n-2,-1,-1):
  A[i]=min(A[i],A[i+1]+1)
 print(*A)
