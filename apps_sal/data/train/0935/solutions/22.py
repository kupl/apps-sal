# cook your dish here
t=int(input())
for i in range(t):
 x=int(input())
 r=x%10
 if(r==0):
  print(0)
 elif(r==5):
  print(1)
 else:
  print(-1)

