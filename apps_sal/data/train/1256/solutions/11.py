# cook your dish here
for _ in range(int(input())):
 N=int(input())
 arr=list(map(int,input().split()))
 x=0
 y=0
 for i in arr:
  if(i==2):
   x+=1
  if(i>2):
   y+=1
 print(x*y + (y*(y-1))//2)
