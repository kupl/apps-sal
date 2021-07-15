# cook your dish here
MOD = (10**9) + 7

def binomialCoefficient(n, k): 
 # since C(n, k) = C(n, n - k) 
  # Declaring an empty array 
 C = [0 for i in range(k+1)] 
 C[0] = 1 #since nC0 is 1 
 
 for i in range(1,n+1): 
 
  # Compute next row of pascal triangle using 
  # the previous row 
  j = min(i ,k) 
  while (j>0): 
   C[j] = C[j] + C[j-1] 
   j -= 1
 
 return int(C[k] )

for _ in range(int(input())):
 
 n , k = list(map( int, input().split()))
 
 arr = list( map( int, input().split()) )
 
 arr = sorted(arr)
 
 value = binomialCoefficient(n-1,k-1)
 
 ans = 1
 
 
 
 for x in range(1,n-1):
  
  if (n - x - 1) >= (k-1) :
   
   temp1 = binomialCoefficient(n-x-1,k-1)
  else:
   temp1 = 0
   
  if x >= (k-1):
   
   temp2 = binomialCoefficient(x,k-1)
  else:
   temp2 = 0 
   
   
  # print(value,ans,temp1,temp2)
  ans = ( ans * (arr[x]**( value - temp2 - temp1 )) )%MOD
  
 print(ans)
   
  
  
 

