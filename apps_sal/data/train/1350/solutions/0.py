m= 1000000007
def mul(a,b):
 return [(a[0]*b[0]+a[1]*b[2])%m,
   (a[0]*b[1]+a[1]*b[3])%m,
   (a[2]*b[0]+a[3]*b[2])%m,
   (a[2]*b[1]+a[3]*b[3])%m] 
def f(n):
 if n==0:
  return 0
 v1, v2, v3 = 1, 1, 0 
 for rec in bin(n)[3:]:
  v2=v2%m
  v1=v1%m
  v3=v3%m
  calc = (v2*v2)
  v1, v2, v3 = (v1*v1+calc), ((v1+v3)*v2), (calc+v3*v3)
  if rec=='1': v1, v2, v3 = v1+v2, v1, v2
 return [v1+1,v2,v2,v3+1]

def q(X,Y):
 nonlocal A
 s = [1,0,0,1]
 for v in A[X-1:Y]:
  s = mul(s,f(v))
 return s[1]%m

N,M = list(map(int,input().split()))
A=list(map(int,input().split()))
for _ in range(M):
 [T,X,Y] = input().split()
 X,Y = int(X),int(Y)
 if T=='Q':
  print(q(X,Y))
 else:
  A[X-1]=Y
