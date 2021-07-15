def __gcd(a, b): 
  
 # Everything divides 0  
 if (a == 0 or b == 0): 
  return 0; 
 
 # base case 
 if (a == b): 
  return a; 
 
 # a is greater 
 if (a > b): 
  return __gcd(a - b, b); 
 return __gcd(a, b - a); 
 
# Function to find  
# number of squares 
def NumberOfSquares(x, y): 
  
 # Here in built PHP 
 # gcd function is used 
 s = __gcd(x, y); 
 
 ans = (x * y) / (s * s); 
 
 return int(ans);
 
n=int(input())
while n:
 n=n-1
 c,d=map(int,input().split())
 print(NumberOfSquares(c, d))
