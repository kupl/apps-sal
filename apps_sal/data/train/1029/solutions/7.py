T=int(input())
for i in range(T):
 N,K=map(int,input().split())
 L=list(map(int,input().split()))[:K]
 A,C,D=[],[],[]
 for j in range(1,N+1):
  if j not in L:
   A.append(j)
 for k in range(len(A)):
  if k % 2 == 0:
   C.append(A[k])
  else:
   D.append(A[k])
 for j in C:
  print(j,end=" ")
 print()
 for k in D:
  print(k,end=" ")
 print()
