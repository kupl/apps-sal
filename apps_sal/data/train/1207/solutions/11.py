# cook your dish here
t=int(input())

def kingship(p,n):
 
 s=0
 p=sorted(p)
 
 for i in range(1,n):
  s+=p[0]*p[i]
 return s
for _ in range(t):
 n=int(input())
 p=list(map(int,input().split()))
 
 r=kingship(p,n)
 print(r)
