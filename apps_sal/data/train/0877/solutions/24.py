try:
 t=int(input())
 while(t):
  x,y,k,n=input().split()
  n=int(n)
  k=int(k)
  x=int(x)
  y=int(y)
  if (x-y)%(2*k)==0:
   print("Yes")
  else:
   print("No")
   
  t-=1
except:
 pass
