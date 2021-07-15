t=eval(input(""))
for i in range (0,t):
 num = list(map(int, input().split()))
 n=num[0]
 b=num[1]
 m=num[2]
 h=0
 tt=0
 f=0
 while(n>1):
  h+=1
  if n%2==0:
   f=n/2
  else:
   f=(n+1)/2
  if h>1:
    m=2*m
  tt=tt+f*m+b
  # print("tt",tt," n ", n)
  n=n-f
 if n==1:
  if h>1:
   tt=tt+2*n*m
  else:
   tt=tt+n*m
  #print("tt ",tt," n",n)
 print(tt)
   

