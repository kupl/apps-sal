# cook your dish here
t=int(input())
for i in range(t):
 k=0
 n=int(input())
 l=list(map(int,input().split()))
 max=l[0]
 for j in range(n):
  if l[j]<=max:
   k=k+1
   max=l[j]
 print(k)
