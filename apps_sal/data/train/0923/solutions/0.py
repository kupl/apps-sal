t=int(input())
while(t):
 k=1
 j=0
 n=int(input())
 while(n>0):
  if(n<=k):
   j+=1
   n=0
  elif n>2*k:
   j+=2
   n=n-2*k
   k+=1
  else:
   j+=2
   n=0
 print(j)
 t-=1
