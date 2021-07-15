t = int(input())

while(t>0):
 
 n=int(input())
 if(n<=0):
  print(0)
 
 fact=1
 start=1
 for i in range(1,n+1):
  fact*=start
  start+=2
 print(fact)
 
 t=t-1

