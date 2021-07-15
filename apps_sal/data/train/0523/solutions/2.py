# cook your dish here
MOD = (10**9) + 7

def ncr(n, r, p): 
 # initialize numerator 
 # and denominator 
 num = den = 1 
 for i in range(r): 
  num = (num * (n - i)) % p 
  den = (den * (i + 1)) % p 
 return (num * pow(den,  
   p - 2, p)) % p 

for _ in range(int(input())):
 
 n , k = list(map( int, input().split()))
 
 arr = list( map( int, input().split()) )
 
 arr = sorted(arr)
 
 value = ncr(n-1,k-1,MOD)
 
 ans = 1
 
 
 
 for x in range(1,n-1):
  
  if (n - x - 1) >= (k-1) :
   
   temp1 = ncr(n-x-1,k-1,MOD)
  else:
   temp1 = 0
   
  if x >= (k-1):
   
   temp2 = ncr(x,k-1,MOD)
  else:
   temp2 = 0 
   
   
  # print(value,ans,temp1,temp2)
  ans = ( ans * (arr[x]**( value - temp2 - temp1 )) )%MOD
  
 print(ans)
   
  
  
 

