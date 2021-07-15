try:
 T=int(input())
 P=""
 for i in range (T):
  N=int(input())
  A=[[0 for i in range (N)]for j in range(N)]
  a=1
  K=0
  for x in range(2*N):
   if K<N:
    i=0
    j=K
    for y in range (K+1):
     if i+j==K and i>=0 and j>=0:
      A[i][j]=a
      i=i+1
      j=j-1
      a=a+1
    K=K+1
   else:
    J=N-1
    I=K-(J)
    for y in range(2*N-K-1):
     A[I][J]=a
     I=I+1
     J=J-1
     a=a+1
    K=K+1
  for a in range(0,N):
   for b in range(0,N):
    if b!=N-1:
     P=P+str(A[a][b])+" "
    else:
     P=P+str(A[a][N-1])+"\n"
 print(P)
except:
 pass
