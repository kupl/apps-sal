# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s=0
 for i in range(n):
  p,q,d=map(int,input().split())
  x=(d/100)*p
  pr=p+x 
  y=pr-((d/100)*pr)
  l=p-y
  tl=q*l 
  s=s+tl
 print(s)
