# cook your dish here
t=int(input())
for _ in range(t):
 n=int(input())
 m=list(map(int,input().split()))
 temp,speed=m[0],m[0]
 for i in range(1,n):
  if temp<m[i]:
   speed+=m[i]-temp
   temp=speed-i-1
  else:
   temp-=1 
 print(speed)
 

