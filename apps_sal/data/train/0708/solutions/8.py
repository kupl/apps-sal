# cook your dish here
z=int(1e9+7)
for i in range (int(input())):
 n,a=map(int,input().split())
 x=0
 for j in range(n):
  c=pow(a,(2*j)+1,z)
  x+=c
  x=x%z
  a=a*c
  a=a%z
 print(x)
