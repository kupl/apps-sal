# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=0
 for i in range(n):
  a,j=map(int,input().split())
  if j-a >5:
   s=s+1 
 print(s)
