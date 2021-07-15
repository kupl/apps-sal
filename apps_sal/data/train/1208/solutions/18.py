def cal(n):
 prod = 1
 fac = 1
 for i in range(1,n+1):
  fac*=i
  fac = fac%1000000007 
  prod*=fac
  prod = prod%1000000007
 print(prod)

t = int(input())
while t:
 prod = 1
 fac = 1
 t-=1
 n = int(input())
 cal(n)
