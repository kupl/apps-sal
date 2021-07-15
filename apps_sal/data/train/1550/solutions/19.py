import math 
 
def swap(a,b): 
 
 temp=a 
 a=b 
 b=temp 
 
# log(n) solution 
def xnor(a, b): 
  
 # Make sure a is larger 
 if (a < b): 
  swap(a, b) 
 
 if (a == 0 and b == 0) : 
  return 1; 
  
 # for last bit of a 
 a_rem = 0 
  
 # for last bit of b 
 b_rem = 0 
 
 # counter for count bit and  
 #  set bit in xnor num 
 count = 0
  
 # for make new xnor number 
 xnornum = 0 
 
 # for set bits in new xnor 
 # number 
 while (a!=0) : 
  
  # get last bit of a 
  a_rem = a & 1 
   
  # get last bit of b 
  b_rem = b & 1 
 
  # Check if current two  
  # bits are same 
  if (a_rem == b_rem):      
   xnornum |= (1 << count) 
   
  # counter for count bit 
  count=count+1
   
  a = a >> 1
  b = b >> 1
  
 return xnornum;

def nthXorFib(n, a, b): 
 if n == 0 :  
  return a 
 if n == 1 :  
  return b 
 if n == 2 :  
  return a ^ b 
 
 return nthXorFib(n % 3, a, b)

def nthXNorFib(n, a, b): 
 if n == 0 :  
  return a 
 if n == 1 :  
  return b 
 if n == 2 :  
  return xnor(a, b)
 
 return nthXNorFib(n % 3, a, b)

for test in range(int(input())):
 a, b, n = map(int, input().split())

 print(max(nthXNorFib(n - 1, a, b), nthXorFib(n - 1, a, b)))
