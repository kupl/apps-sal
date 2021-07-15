# cook your dish here
t=int(input())
for _ in range(t):
 s=0
 n=int(input())
 while(n>0):
  s+=(n*n)
  n-=2
 print(s)
