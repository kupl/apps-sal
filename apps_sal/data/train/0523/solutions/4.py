# cook your dish here
MOD = (10**9) + 7

def binomialCoefficient(n, r, p): 

 # The array C is going to store last row of 
 # pascal triangle at the end. And last entry 
 # of last row is nCr. 
 C = [0 for i in range(r+1)] 
 
 C[0] = 1 # Top row of Pascal Triangle 
 
 # One by constructs remaining rows of Pascal 
 # Triangle from top to bottom 
 for i in range(1, n+1): 
 
  # Fill entries of current row  
  # using previous row values 
  for j in range(min(i, r), 0, -1): 
 
   # nCj = (n - 1)Cj + (n - 1)C(j - 1) 
   C[j] = (C[j] + C[j-1]) % p 
 
 return int(C[r])

for _ in range(int(input())):
 
 n , k = list(map( int, input().split()))
 
 arr = list( map( int, input().split()) )
 
 arr = sorted(arr)
 
 value = binomialCoefficient(n-1,k-1,MOD)
 
 ans = 1
 
 
 
 for x in range(1,n-1):
  
  if (n - x - 1) >= (k-1) :
   
   temp1 = binomialCoefficient(n-x-1,k-1,MOD)
  else:
   temp1 = 0
   
  if x >= (k-1):
   
   temp2 = binomialCoefficient(x,k-1,MOD)
  else:
   temp2 = 0 
   
   
  # print(value,ans,temp1,temp2)
  ans = ( ans * (arr[x]**( value - temp2 - temp1 )) )%MOD
  
 print(ans)
   
  
  
 

