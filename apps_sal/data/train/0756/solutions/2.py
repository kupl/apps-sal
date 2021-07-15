# cook your dish here
def prime(n):
 for i in range(2,(n//2)+1):
  if(n%i ==0):
   return("no")
   break
 else:
  return("yes")
for i in range(int(input())):
 a,b=map(int,input().split())
 x=a+b+1
 while(1):
  if(prime(x)=="yes"):
   ans=x
   break
  else:
   x+=1
 print(x-(a+b))
