# cook your dish here
def binaryToDecimal(binary): 
  
 binary1 = binary 
 decimal, i, n = 0, 0, 0
 while(binary != 0): 
  dec = binary % 10
  decimal = decimal + dec * pow(2, i) 
  binary = binary//10
  i += 1
 return decimal
def add(a,b):
 count=0
 u=0
 v=0
 while b>0:
  u=a^b
  v=a&b
  a=u
  b=v*2
  count = count+1
 return count
t=int(input())
while t!=0:
 a = int(input())
 b = int(input())
 a=int(binaryToDecimal(a))
 b=int(binaryToDecimal(b))
 #print(a)
 #print(b)
 print(add(a,b))
 t=t-1

