# cook your dish here
for i in range(int(input())):
 c=0
 a,b=map(int,input().split())
 for j in range(a,b+1):
  k=j%10
  if k==2 or k==3 or k==9:
   c=c+1
 print(c)
