def increasing_numbers(n):
   return fac(n+9)/(fac(9)*fac(n))

def fac(n):
   c=1
   for i in range(2,n+1):
      c*=i
   return c
