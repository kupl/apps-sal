# cook your dish here
a=int(input())
z=0
for i in range(a):
 b=list(map(int,input().split()))
 y=0
 for j in b:
  if j==1:
   y=y+1
 if y>1:
  z=z+1
print(z) 
