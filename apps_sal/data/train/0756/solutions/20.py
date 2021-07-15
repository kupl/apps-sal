t=int(input())
for i in range(t):
 p1,p2=list(map(int,input().split()))
 num=p1+p2
 a=1
 

 while True:
  prime=num+a
  r=0
  for i in range(2,int(prime**0.5)+1):
   if prime%i==0:
    a+=1
    r=1
    break
  if r==0:
   print(a)
   break


  

  


