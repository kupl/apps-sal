# cook your dish here
def __gcd(a, b): 
 if (a == 0 or b == 0): 
  return 0; 
 if (a == b): 
  return a; 
 if (a > b): 
  return __gcd(a - b, b); 
 return __gcd(a, b - a); 
for _ in range(int(input())):
 x,y=list(map(int,input().split()))
 s = __gcd(x, y); 
 ans = (x * y) / (s * s); 
 print(int(ans))

