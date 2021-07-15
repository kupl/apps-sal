L=1000000007
def pow(a,b):
 if b==0:
  return 1
 elif b==1:
  return a
 else:
  nonlocal L
  x=pow(a,b//2)
  y=pow(a,b%2)
  r=(x*x)%L
  r=(r*y)%L
  return r
for i in range(int(input())):
 N=int(input())
 p=pow(3,N)+3 if N%2==0 else pow(3,N)-3
 print(p)

