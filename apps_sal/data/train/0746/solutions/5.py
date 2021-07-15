while 1:
 N=eval(input())
 if N==0:
  break
 A=list(map(int,input().split(' ')))
 for i in range(N-1,0,-1):
  C=1<<(i-1)
  B=1<<i
  for j in range(C-1,B-1,1):
   A[j]=A[j]*max(A[2*j+1],A[2*j+2])
 print(A[0]%1000000007)

