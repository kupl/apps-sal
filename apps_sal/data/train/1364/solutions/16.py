T=int(input())
for i in range(T):
 a=input().split()
 N=int(a[0])
 c=int(a[1])
 D={}
 for j in range(N):
  b=input().split()
  x=int(b[0])
  y=int(b[1])
  t=(x-y,x%c)
  try:
   D[t]+=[x//c]
  except:
   D[t]=[x//c]
 q=len(D)
 p=0
 for k in list(D.values()):
  L=k
  L.sort()
  w=len(L)
  A=L[:(w)//2]
  B=L[(w+1)//2:]
  p+=sum(B)-sum(A)
 print(q,p)

