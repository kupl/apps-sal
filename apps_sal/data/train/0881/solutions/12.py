# cook your dish here
x=int(input())
for i in range(x):
 y=int(input())
 l=list(map(int,input().split()))
 c=[1]*y
 for j in range(y-1):
  if l[j]<=l[j+1]:
   c[j+1]=c[j]+1
 print(sum(c))
