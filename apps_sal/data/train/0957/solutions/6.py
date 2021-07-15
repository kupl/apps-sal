T=int(input())
for _ in range (T):
 N=int(input())
 A=list(map(int,input().split()))
 A.sort()
 mv=max(A[1]-A[0],A[N-1]-A[N-2])
 for i in range(1,N-1):
  a=min(A[i+1]-A[i],A[i]-A[i-1])
  mv=max(a,mv)
 print(mv)

