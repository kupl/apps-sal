# cook your dish here
p=int(input())
for z in range(p):
 n=int(input())
 a=[]
 for i in range(8):
  a.append(0)
 for i in range(n):
  x,y=list(map(int,input().split()))
  if x<=8 and y>a[x-1]:
   a[x-1]=y
 print(sum(a))

