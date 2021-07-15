def closestNumber(n, m) : 
# Find the quotient 
 q = int(n / m) 
 
# 1st possible closest number 
 n1 = m * q 
 
# 2nd possible closest number 
 if((n * m) > 0) : 
  n2 = (m * (q + 1)) 
 else : 
  n2 = (m * (q - 1)) 
  
 # if true, then n1 is the required closest number 
 if (abs(n - n1) < abs(n - n2)) : 
  return n1 
  
 # else n2 is the required closest number  
 return n2 

T = int(input())
for j in range(1, T+1):
 N, B = input().split()
 N = int(N)
 B = int(B)
 p = N % B
 k = N
 fs = 0
 maxim = 0
 
 print(int((N-closestNumber(int(N/2), B))*(closestNumber(int(N/2), B))/B))
  
  

