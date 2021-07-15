# cook your dish here
n=int(input())
for i in range(n):
 m=int(input())
 l=[0]*8
 for i in range(m):
  a,b=map(int,input().split())
  if a>0 and a<=8:
   if l[a-1]<b:
    l[a-1]=b
 print(sum(l))
