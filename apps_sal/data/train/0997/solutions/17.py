# cook your dish here
t=int(input())
for i in range(0,t):
 a=list(map(int,input().split()))
 m=[10]*a[0]
 
 for j in range(0,a[1]):
  b=list(map(int,input().split()))
  for k in range(b[0]-1,b[1]):
   m[k]=m[k]*b[2]
 l=sum(m)
 print(l//a[0])

