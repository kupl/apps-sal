t = int(input())

def xnor(a, b): 
  
 # Make sure a is larger 
 if (a < b): 
  a, b = b, a
 
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

while t:
 t -= 1

 a, b, n = input().split()
 a, b, n = int(a), int(b), int(n)

 if n%3 == 1:
  print(a)
  continue

 if n%3 == 2:
  print(b)
  continue

 xor_ = a ^ b
 xnor_ = xnor(a, b)

 print(max(xor_, xnor_))
