try:

 t=int(input())
 for i in range(t):
  n,k,v=list(map(int,input().split()))
  a=[int(x) for x in input().split()]
  p=0
  A=sum(a)
  p=int((v*(n+k)-A)/k)
  if((p>0) and ((v*(n+k)-A)%k)==0 ):
   print(p)
  else:
   print("-1")
   
except EOFError:
 pass

 

 


