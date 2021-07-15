# cook your dish here
def val(c): 
 if c >= '0' and c <= '9': 
  return ord(c) - ord('0') 
 else: 
  return ord(c) - ord('A') + 10; 

# Function to convert a number 
# from given base 'b' to decimal 
def toDeci(str,base): 
 llen = len(str) 
 power = 1 #Initialize power of base 
 num = 0 #Initialize result 

 # Decimal equivalent is str[len-1]*1 + 
 # str[len-1]*base + str[len-1]*(base^2) + ... 
 for i in range(llen - 1, -1, -1): 
  
  # A digit in input number must 
  # be less than number's base 
  if val(str[i]) >= base: 
   print('Invalid Number') 
   return -1
  num += val(str[i]) * power 
  power = power * base 
 return num 

t=int(input())
for _ in range(t):
 s=input()
 s1=[]
 
 for i in range(len(s)):
  if s[i]=='a'or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u':
   s1.append(1)
  else:
   s1.append(0)
 s2=''.join([str(elem) for elem in s1]) 
 print(toDeci(s2, 2)) 

   

