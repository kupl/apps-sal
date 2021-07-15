t=int(input())
i=0
while i<t:
 n=int(input())
 j=n
 b=0
 while n>0 :
  r=int(n**(0.5))
  b+=1
  n=n-r**2
 print(b)
 i+=1
