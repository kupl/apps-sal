# cook your dish here
import math
def isPowerOfTwo(y):
 return math.ceil(math.log(y, 2)) == math.floor(math.log(y, 2))

test=int(input())
for _ in range(test):
 n=int(input())
 a=[]
 if n==1:
  a.append(1)
 if isPowerOfTwo(n) and n!=1:
  print("-1")
 if n>=3 and not (isPowerOfTwo(n)):
  a.append(2)
  a.append(3)
  a.append(1)
 if n>3 and not (isPowerOfTwo(n)):
  i=4
  while i<=n:
   if isPowerOfTwo(i):
    a.append(i+1)
    a.append(i)
    i=i+2
   else:
    a.append(i)
    i=i+1
 print(*a)
