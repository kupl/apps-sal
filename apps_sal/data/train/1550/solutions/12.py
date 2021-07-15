
def togglebit( n): 
 
 if (n == 0): 
  return 1

 i = n 

 n = n|(n >> 1) 

 n |= n >> 2
 n |= n >> 4
 n |= n >> 8
 n |= n >> 16
 
 return i ^ n 
  
def xnor( num1, num2): 
  
 if (num1 < num2): 
  temp = num1 
  num1 = num2 
  num2 = temp 
 num1 = togglebit(num1) 
  
 return num1 ^ num2 
def nthXorFib(n, a, b): 
 if n == 0 :  
  return a 
 if n == 1 :  
  return b 
 if n == 2 :  
  return a ^ b 
 
 return nthXorFib(n % 3, a, b) 
def nthXnorFib(n, a, b): 
 if n == 0 :  
  return a 
 if n == 1 :  
  return b 
 if n == 2 :  
  return xnor(a,b)
 
 return nthXnorFib(n % 3, a, b) 
 
t=int(input())
while(t):
 a,b,n=map(int,input().split())
 print(max(nthXnorFib(n-1,a,b),nthXorFib(n-1,a,b)))
 t-=1
