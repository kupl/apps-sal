N,K=map(int,input().split())
#1 2 3...N
if N%2==0:
  L=[str(N)]*K
  L[0]=str(N//2)
  print(" ".join(L))
  return
#L[0]=N//2+1
#N//2のずれ？
L=[(N//2)+1]*K
for i in range(K//2):
  if L[-1]==1:
    L.pop(-1)
  elif len(L)!=K:
    L[-1]-=1
    L+=[N]*(K-len(L))
  else:
    L[-1]-=1
L=list(map(str,L))
print(" ".join(L))
