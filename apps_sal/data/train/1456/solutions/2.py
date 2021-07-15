import math 
from collections import defaultdict
def IsPowerOfTwo(x):
 return (x != 0) and ((x & (x - 1)) == 0)

def getFirstSetBitPos(n): 
  return int(math.log2(n&-n)+1)-1

def xpr(n):
 if IsPowerOfTwo(n): 
  return (-1, -1)
 # Has the first set bit from lsb
 index = getFirstSetBitPos(n)
 # print("Index : ", index)
 # Convert the number to binary string
 binary_n_string = str(bin(n))[2:]
 # print(binary_n_string)
 a = ""
 b = ""
 i = 0
 for bit in reversed(binary_n_string):
  if i < index:
   a = '0' + a
   b = '0' + b
  elif i == index:
   a = '1' + a
   b = '0' + b
  else:
   if bit == '0':
    a = '0' + a
    b = '0' + b
   else:
    a = '0' + a
    b = '1' + b
  i = i + 1
 a, b = int(a, 2), int(b, 2)
 return (a, b)
 
 
def glr(x):
 tot = (x*(x+1))//2
 lb = 0
 while x >= 1:
  tot -= int(((x+1)//2)*2**lb)
  lb += 1
  tot -= 1
  x = x / 2
 return tot 
 
t = int(input())
while t > 0:
 l, r = list(map(int,input().split()))
 sumt = 0
 # dict1 = defaultdict(int)
 # for i in range(l, r+1):
 #   val = xpr(i)
 #   if val[1] != -1 and i%2 == 0:
 #       dict1[val[1]] += 1
 #   # print(i, val)
 #   sumt += val[1]
 
 print(glr(r) - glr(l-1))
 t = t - 1
