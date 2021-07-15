MOD = 10**9 + 7

for _ in range(int(input())):
 n,a = list(map(int,input().split()))

 res = 0

 base = a
 for i in range(n):
  curr = pow(base,2*i+1,MOD)
  res+=curr
  res%=MOD
  base = base*curr
  base%=MOD
 
 print(res%MOD)

  
  


 



 

