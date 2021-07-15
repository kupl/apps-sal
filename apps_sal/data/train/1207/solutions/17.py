# cook your dish here
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 x=min(l)
 y=0
 for i in l:
  if i!=x:
   y+=i*x 
 print(y)

