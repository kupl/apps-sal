# cook your dish here
def gcd(x, y):
 while y:
  x, y = y, x % y
 return x

def lcm(x, y):
 return (x*y)//(gcd(x,y))

def isPrime(n) : 
 if (n <= 1) : 
  return False
 if (n <= 3) : 
  return True
 if (n % 2 == 0 or n % 3 == 0) : 
  return False
 i = 5
 while(i * i <= n) : 
  if (n % i == 0 or n % (i + 2) == 0) : 
   return False
  i = i + 6
 return True

abc="abcdefghijklmnopqrstuvwxyz"

pi=3.141592653589793238


def find_common(a):
 gcd_ = a[0]
 for i in range(1,len(a)):
  gcd_ = gcd(gcd_,a[i])
 return(gcd_)


t = int(input())
for _ in range(t):
 n = int(input())
 arr = list(map(int,input().split()))
 total = sum(arr)
 
 unit_size = find_common(arr)
 units = 0
 for i in arr:
  units = units + i//unit_size
 print(unit_size,units)
 
 
 
 
 
 
 
 
 
 

