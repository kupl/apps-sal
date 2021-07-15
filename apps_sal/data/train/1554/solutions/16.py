t=int(input())
for _ in range(t):
 a,b=list(map(int,input().split()))
 while a!=0 and b!=0 and a!=b:
  if(a>b):
   a=a%b
  else:
   b=b%a
 if(a==0 or b==0):
  print((a+b)*2)
 elif(a==b):
  print(a+b)

