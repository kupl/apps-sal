T=int(input())
for i in range(T):
 N,K,L=map(int,input().split())
 if K*L<N:
  print(-1)
 elif (K==1 and N>1):
  print(-1)
 else:
  for j in range(N):
   print((j%K)+1,end=' ')
  print()
